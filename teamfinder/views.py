# Create your views here.
import json
from django.db.backends.sqlite3.base import IntegrityError
from django.http import QueryDict
import traceback
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
        new_team.members.add(owner)
        new_team.save()
        assignment.teams.add(new_team)
        assignment.save()

        teams = assignment.teams.all()
        return Response(serializers.serialize('json', teams), status=status.HTTP_201_CREATED)


class GenerateTeams(APIView):
    # For debug only
    # def get(self, request):
    # Teams = Team.objects.all();
    # return Response(Teams)

    def post(self, request):
        which_assignment = request.data.get('which_assignment')
        assignment = Assignment.objects.get(pk=which_assignment)
        course = Course.objects.get(pk=assignment.course_fk.pk)
        new_Team = Team.objects.create(name='Generated Team', number=1)
        assignment.teams.add(new_Team)
        assignment.save()
        students = course.students.all()
        which_team = 1

        # Partition into four each
        students_added = 0
        for student in students:
            # Create new Team every 4 students
            if students_added % 4 == 0 and students_added != 0:
                new_Team = Team.objects.create(name='Generated Team', number=2 + students_added / 4)
                assignment.teams.add(new_Team)
                assignment.save()
                which_team += 1

            # Add student to the Team
            new_Team.members.add(student)
            new_Team.save()
            students_added += 1

        assignment.teams.add(new_Team)
        assignment.save()
        teams = assignment.teams.all()
        return Response(serializers.serialize('json', teams), status=status.HTTP_201_CREATED)


class CourseAdd(APIView):
    def delete(self, request, pk, format=None):
        which_course = Course.objects.get(pk=pk)
        which_course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
        asdf = assignment.teams.all()
        for x in asdf:
            for y in x.members.all():
                print y.email
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


# Return questions for given course
class QuestionView(generics.ListCreateAPIView, generics.DestroyAPIView):
    serializer_class = QuestionSerializer

    def delete(self, request, *args, **kwargs):
        return Response(status=status.HTTP_200_OK)

    def get_queryset(self):
        if 'which_course' in self.kwargs:
            which_course = self.kwargs['which_course']
            return Question.objects.filter(course_fk=which_course)
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

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        # return (permissions.IsAuthenticated(), IsAccountOwner(),)
        # TODO
        return False

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
