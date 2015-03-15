# Create your views here.
from heapq import *
import json
from django.db.backends.sqlite3.base import IntegrityError
from django.http import QueryDict
import traceback
import itertools
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import generics
from django.contrib.auth import authenticate, login, logout
import StringIO
from rest_framework import permissions, views, viewsets
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from teamfinder.serializers import *
import copy
from django.core import serializers
from teamfinder.models import *
from rest_framework.permissions import BasePermission, SAFE_METHODS


class CourseUpload(APIView):
    def post(self, request):
        the_pk = request.data.get('pk')
        course = Course.objects.get(pk=the_pk)
        up_file = request.FILES['import_csv']
        filestream = StringIO.StringIO(up_file.read())
        # serializer = CourseSerializer(data=request.data)
        # if serializer.is_valid():
        for row in filestream.read().splitlines():
            cols = row.split(',')
            try:
                my_pk = 'STUDENT|' + cols[1]
            except IndexError:
                return Response('Bad input', status=status.HTTP_400_BAD_REQUEST)

            try:
                the_user = User.objects.get(pk=my_pk)
                course.students.add(the_user)
                course.save()
            except:
                # Student not in system yet, add as Placeholder

                # Check if placeholder yet
                placeholder = User.objects.create_user(cols[1], 'PLACEHOLDER', name=cols[0])
                course.students.add(placeholder)
                course.save()

        return Response('Good for you Jerry :)', status=status.HTTP_201_CREATED)


class AddTeam(APIView):
    def put(self, request):
        which_team = request.data.get('which_team')
        which_student = request.data.get('which_student')
        which_action = request.data.get('which_action')
        which_field = request.data.get('which_field')
        field_value = request.data.get('field_value')
        team = Team.objects.get(pk=which_team)

        if which_action == 'update':
            if which_field == 'name':
                team.name = field_value
            if which_field == 'description':
                team.description = field_value
            if which_field == 'lfm':
                team.lfm = field_value
            team.save()
            # return Response(serializers.serialize('json', team), status=status.HTTP_201_CREATED)
            return Response(status=status.HTTP_200_OK)

        user = User.objects.get(type_and_email=which_student)
        if which_action == 'add':
            team.members.add(user)
        elif which_action == 'remove':
            team.members.remove(user)
        team.save()
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        which_assignment = request.data.get('which_assignment')
        team_name = request.data.get('team_name')
        team_description = request.data.get('team_name')
        if team_description is None:
            team_description = ''

        assignment = Assignment.objects.get(pk=which_assignment)
        num_teams = assignment.teams.count()
        if team_name is None:
            team_name = 'Team ' + str(num_teams + 1)

        new_team = Team.objects.create(name=team_name, description=team_description,
                                       number=num_teams + 1)
        owner = request.data.get('owner')
        if 'STUDENT' in owner:
            new_team.members.add(owner)
        new_team.save()
        assignment.teams.add(new_team)
        assignment.save()

        teams = assignment.teams.all()
        return Response(serializers.serialize('json', teams), status=status.HTTP_201_CREATED)


TEAM_MIN = 4  # min number for team TODO


class StudentObj:
    def __init__(self, student):
        self.type_and_email = student.type_and_email

    def __unicode__(self):
        return self.type_and_email


class TeamObj:
    def __init__(self, team, name=None, number=None):
        self.members = []

        if team is not None:
            for member in team.members.all():
                self.members.append(copy.copy(StudentObj(member)))
            self.pk = team.pk
            self.number = team.number
            self.name = team.name
            self.description = team.description
        else:
            self.pk = number
            self.number = number
            self.name = name
            self.description = 'This team was auto-generated.'

    def __unicode__(self):
        return self.pk


class ConfigState:
    def __init__(self, available, teams, parent=None, prev_action=None, g=0, django=True, node_id=0):
        self.node_id = node_id
        self.teams = []
        self.parent = parent
        self.prev_action = prev_action
        for team in teams:
            if django:
                self.teams.append(TeamObj(team))
            else:
                self.teams.append(team)

        self.available = []
        for avail in available:
            self.available.append(StudentObj(avail))

        self.g = g

    @property
    def __unicode__(self):
        ret = '=================================='
        ret += '\n<State: id=' + str(self.node_id) + ", g=" + str(self.g) + ', parent=' + str(
            self.parent) + ', prev_action=' + str(
            self.prev_action) + '>'
        ret += '\n'
        ret += 'Teams:\n'
        for team in self.teams:
            ret += 'Team ' + str(team.pk)
            ret += '\n-----------------------------\n'
            for member in team.members:
                ret += member.type_and_email
                ret += '\n'
            ret += '\n'

        ret += 'Available:\n'
        for x in self.available:
            ret += str(x.type_and_email)
            ret += '\n'
        ret += '\n'
        ret += '=================================='
        return ret


def goodness(new_teams):
    return 0


class GenAlgorithm():
    # initial state
    def __init__(self, available, teams):
        self.initState = ConfigState(available, teams)
        self.node_id = 0
        self.num_students = len(available)
        for team in teams:
            self.num_students += team.members.all().count()  # TODO test

    def get_children(self, state):
        children = []
        cstate = state[1]
        teams = copy.deepcopy(cstate.teams)
        available = cstate.available

        # Add reduce states (Combining group)
        for i, j in itertools.combinations(range(len(teams)), 2):
            # Merge team[i] and team[j]
            # new_teams = teams[:]  # make copy of it
            # Make deep copy brah
            new_teams = copy.deepcopy(teams)
            for x, team in enumerate(new_teams):
                team.members = copy.deepcopy(teams[x].members)

            # Iterate all members in team[j] and add to team[i]
            for member in new_teams[j].members:
                new_teams[i].members.append(member)
            del new_teams[j]
            self.node_id += 1
            new_g = state[0] + goodness(new_teams)
            new_state = ConfigState(available, new_teams, g=new_g, django=False, parent=cstate.node_id,
                                    prev_action='reduce', node_id=self.node_id)
            children.append(new_state)

        # Add create state
        # only create if teams less than students / 4
        # could be none avail
        if len(teams) < (self.num_students / TEAM_MIN) / 2 + 1 and len(cstate.available) > 0:
            next_student = cstate.available[0]
            new_available = cstate.available[1:]
            new_teams = copy.deepcopy(teams)
            new_teams.append(TeamObj(team=None, name='Generated Group', number=len(teams) + 1))
            new_teams[len(new_teams) - 1].members.append(next_student)
            self.node_id += 1
            new_g = state[0] + goodness(new_teams)
            new_state = ConfigState(new_available, new_teams, django=False, g=new_g, parent=cstate.node_id,
                                    prev_action='create', node_id=self.node_id)
            children.append(new_state)

        # Add shift states
        if len(teams) > 0 and len(cstate.available) > 0:
            next_student = cstate.available[0]
            del cstate.available[0]
            for i in range(len(teams)):
                new_teams = copy.deepcopy(teams)
                for x, team in enumerate(new_teams):
                    team.members = copy.deepcopy(teams[x].members)
                new_teams[i].members.append(next_student)
                self.node_id += 1
                new_g = state[0] + goodness(new_teams)
                new_state = ConfigState(cstate.available, new_teams, django=False, g=new_g, parent=cstate.node_id,
                                        prev_action='shift ' + next_student.type_and_email, node_id=self.node_id)
                children.append(new_state)

        return children

    def is_goal(self, state):
        # Check team balanced
        for team in state[1].teams:
            # TODO come up with better goal (calc students in class / 4), add heuristic of teamsize sq distance
            if len(team.members) < TEAM_MIN:
                return False

        # Check all assigned
        return len(state[1].available) == 0

    def search(self):
        frontier = []
        i = 0
        heappush(frontier, (i, self.initState))
        while True:
            try:
                current = heappop(frontier)
                if self.is_goal(current) or current[0] > 8:
                    self.is_goal(current)
                    # print current[1].__unicode__
                    break
                # Append children
                children = self.get_children(current)
                for child in children:
                    heappush(frontier, (child.g, child))
            except Exception as exc:
                print exc.message
                self.get_children(current)
                return None
        return current


class GenerateTeams(APIView):
    def post(self, request):
        which_assignment = request.data.get('which_assignment')
        assignment = Assignment.objects.get(pk=which_assignment)
        course = Course.objects.get(pk=assignment.course_fk.pk)

        # Initialize to all students
        available = {}
        for student in course.students.all():
            available[student] = StudentObj(student)

        # Remove students that have a team. Fill in (members, team) into tuple array as well.
        teams = assignment.teams.all()
        for team in teams:
            for member in team.members.all():
                del available[member]

        algo = GenAlgorithm(available.keys(), teams)
        result = algo.search()
        if result is None:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        assignment.teams.all().delete()
        for team in result[1].teams:
            members = User.objects.filter(type_and_email__in=team.members)
            for student in members:
                student.lfg = False
            new_django_team = Team.objects.create(name=team.name, number=team.number, description=team.description)
            new_django_team.members.add(*members)
            new_django_team.save()
            assignment.teams.add(new_django_team)
            assignment.save()
        teams = assignment.teams.all()
        return Response(serializers.serialize('json', teams), status=status.HTTP_201_CREATED)


class RequestAdd(APIView):
    def put(self, request):
        pk = request.data.get('which_request')
        which_request = JoinRequest.objects.get(pk=pk)
        which_request.delete()
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        serializer = JoinRequestSerializer(data=request.data)
        if serializer.is_valid():
            request = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RequestView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = JoinRequestSerializer

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def get_queryset(self):
        if 'which_team' in self.kwargs:
            which_team = self.kwargs['which_team']
            return JoinRequest.objects.filter(team=which_team)

        return JoinRequest.objects.all()


class CourseAdd(APIView):
    def put(self, request):
        pk = request.data.get('pk')
        which_course = Course.objects.get(pk=pk)
        which_course.delete()
        return Response(status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            course = serializer.save()
            if request.FILES.__len__() > 0:
                up_file = request.FILES['import_csv']
                filestream = StringIO.StringIO(up_file.read())
                for row in filestream.read().splitlines():
                    cols = row.split(',')
                    my_pk = 'STUDENT|' + cols[1]
                    try:
                        the_user = User.objects.get(pk=my_pk)
                        course.students.add(the_user)
                        course.save()
                    except:
                        # Student not in system yet, add as Placeholder
                        placeholder = User.objects.create_user(cols[1], 'PLACEHOLDER')
                        course.students.add(placeholder)
                        course.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AddThing(generics.ListCreateAPIView):
    serializer_class = ThingSerializer
    queryset = Thing.objects.all()


# Return list for a given professor
class CourseList(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        return Course.objects.filter(course_professor='INSTRUCTOR|' + self.kwargs['prof'])

    authentication_classes = (SessionAuthentication, BasicAuthentication)  ## TODO wtf is this for
    # permission_classes = (IsAuthenticated)


# Return rotser for given course pk
class CourseRoster(generics.ListAPIView):
    serializer_class = UserAccountSerializer

    def get_queryset(self):
        course = Course.objects.get(pk=self.kwargs['pk'])
        return course.students.all()


# Return rotser for given assignment pk
class CourseTeams(generics.ListAPIView):
    serializer_class = TeamSerializer

    def get_queryset(self):
        # Assignments with course=which_course
        # ass_num = self.kwargs['assignment_number']
        # assignments = Assignment.objects.filter(course_fk=self.kwargs['course_pk'])
        # the_assignment = assignments.all().get(assignment_number=ass_num)
        # return the_assignment.teams.all()
        assignment = Assignment.objects.get(pk=self.kwargs['ass_pk'])
        return assignment.teams.all()
        # return Course.objects.filter(course_professor='INSTRUCTOR|' + self.kwargs['prof'])


# Return list for a given student
class StudentCourseList(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        try:
            which_student = User.objects.get(type_and_email='PLACEHOLDER|' + str(self.kwargs['student']))

            the_email = which_student.type_and_email.split('|')[1]
            new_student = User.objects.create_user(the_email, 'STUDENT')

            query_set = Course.objects.filter(students__exact=which_student)
            for course in query_set:
                course.students.add(new_student)
                course.save()

            which_student.delete()
        except:
            which_student = User.objects.get(type_and_email='STUDENT|' + str(self.kwargs['student']))
            query_set = Course.objects.filter(students__exact=which_student)

        return query_set

        # Case 2: I was registered, and then added
        # return Course.objects.filter(students__in='STUDENT' + which_student)

    authentication_classes = (SessionAuthentication, BasicAuthentication)
    # permission_classes = (IsAuthenticated)


# Return assignments for given course
class AssignmentList(generics.ListAPIView):
    serializer_class = AssignmentSerializer

    def get_queryset(self):
        which_course = self.kwargs['which_course']
        return Assignment.objects.filter(course_fk=which_course)

class AnswersView(generics.ListAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    serializer_class = AnswerSerializer

    def put(self, request, *args, **kwargs):
        user = request.data.get('user_fk')
        weight = request.data.get('weight')
        question = request.data.get('question_fk')
        value = request.data.get('value')

        # Does question have an ansewr?
        queryset = Answer.objects.filter(question_fk=question, user_fk=user)
        if len(queryset) > 0:
            # Exists, so update it
            for x in queryset:
                x.weight = weight
                x.value = value
                x.save()
        else:
            # Create it
            question = Question.objects.get(pk=question)
            user = User.objects.get(type_and_email=user)
            Answer.objects.create(user_fk=user, weight=weight, value=value, question_fk=question)
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        if 'question' in self.kwargs:
            question = self.kwargs['question']
            which_user = 'STUDENT|' + self.kwargs['user']
            queryset = Answer.objects.filter(question_fk=question, user_fk=which_user)
        else:
            queryset = Answer.objects.all()
        if queryset.__len__() == 0:
            return Response({
                                'status': 'No accounts yet',
                                'message': 'No accounts yet brah'
                            }, status=status.HTTP_200_OK)

        serializer = AnswerSerializer(queryset, many=True)
        return Response(serializer.data)
        # return Answer.objects.filter(question_fk=question, user_fk=which_user)

    # def get_queryset(self):
    #     if 'ass' in self.kwargs:
    #         question = self.kwargs['question']
    #         which_user = 'STUDENT|' + self.kwargs['user']
    #         return Answer.objects.filter(question_fk=question, user_fk=which_user)

class QuestionDetailView(generics.UpdateAPIView, generics.DestroyAPIView, generics.ListCreateAPIView):
    serializer_class = QuestionSerializer
    def update(self, request, *args, **kwargs):
        question = Question.objects.get(pk=kwargs.get('pk'))
        which_action = request.data.get('which_action')
        value = request.data.get('value')
        if which_action == 'update':
            question.text = value
            question.save()
        elif which_action == 'delete':
            question.delete()
        return Response(status=status.HTTP_200_OK)

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Question.objects.filter(pk=pk)


# Return questions for given course
class QuestionView(generics.ListCreateAPIView, generics.DestroyAPIView, generics.UpdateAPIView):
    serializer_class = QuestionSerializer

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def get_queryset(self):
        if 'which_ass' in self.kwargs:
            which_ass = self.kwargs['which_ass']
            return Question.objects.filter(ass_fk=which_ass)
        return Question.objects.all()


class StudentList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = StudentSerializer


class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = StudentSerializer


class UserAccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'email'
    queryset = User.objects.all()
    serializer_class = UserAccountSerializer

    def update(self, request, *args, **kwargs):
        which = request.data.get('type_and_email')
        which_field = request.data.get('which_field')
        user = User.objects.get(type_and_email=which)
        the_input = request.data.get('input')

        if which_field == 'linkedin':
            user.linkedin = the_input
        elif which_field == 'github':
            user.github = the_input
        elif which_field == 'bio':
            user.bio = the_input
        elif which_field == 'skills_str':
            user.skills_str = the_input
        elif which_field == 'name':
            user.name = the_input
        elif which_field == 'profile':
            user.profile_img = the_input
        elif which_field == 'lfg':
            user.lfg = the_input

        user.save()
        return Response(status=status.HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        queryset = User.objects.all()
        if queryset.__len__() == 0:
            return Response({
                                'status': 'No accounts yet',
                                'message': 'No accounts yet brah'
                            }, status=status.HTTP_200_OK)

        serializer = UserAccountSerializer(queryset, many=True)
        return Response(serializer.data)


    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
            if len(request.data['skills_str']) > 0:
                for skill in request.data['skills_str'].split(', '):
                    try:
                        the_skill = Thing.objects.get(name=skill)
                    except:
                        the_skill = Thing.objects.create(name=skill)
                    user.skills.add(the_skill)

            user.save()
            return Response(
                serializer.validated_data, status=status.HTTP_201_CREATED
            )
        return Response({
                            'status': 'Bad request',
                            'message': str(serializer.errors)
                        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(views.APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')
        user_type = request.data.get('user_type')
        the_name = request.data.get('name')
        account = authenticate(type_and_email=user_type + '|' + email, email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)
                serialized = UserAccountSerializer(account)
                return Response(serialized.data)
            else:
                return Response({
                                    'status': 'Unauthorized',
                                    'message': 'This account has been disabled.'
                                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                                'status': 'Unauthorized',
                                'message': 'Username/password combination invalid.'
                            }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(views.APIView):
    permissions = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)


class AddStudent(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = StudentSerializer


# Add assignment
# This is currently a ListCreateAPIView for debug purposes, will change to CreateAPIView
class AddAssignment(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AddNotification(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    def get_queryset(self):
        if 'to' in self.kwargs:
            to = 'STUDENT|' + self.kwargs['to']
            return Notification.objects.filter(to_user=to)
        return Notification.objects.all()

class AddLFG(generics.ListCreateAPIView, generics.DestroyAPIView):
    queryset = LFG.objects.all()
    serializer_class = LFGSerializer

# class AddLFM(generics.ListCreateAPIView):
#     queryset = LFM.objects.all()
#     serializer_class = LFMSerializer

