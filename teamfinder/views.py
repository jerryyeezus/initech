# Create your views here.
from django.http import QueryDict
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import generics
from django.contrib.auth import authenticate, login, logout
import StringIO
from rest_framework import permissions, views, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from teamfinder.serializers import *
from rest_framework.permissions import BasePermission, SAFE_METHODS

# class CourseAdd(generics.ListCreateAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

class CourseAdd(APIView):
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
    authentication_classes = (SessionAuthentication, BasicAuthentication) ## TODO wtf is this for
    # permission_classes = (IsAuthenticated)

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

class StudentList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = StudentSerializer


# class GroupAdd(APIView):
#     def post(self, request):
#         serializer = GroupAddSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
        # qdict = QueryDict('')
        # qdict = qdict.copy()
        # qdict.update(request.data)
        # Parse inputted skills
        # Assume comma and space (validate on client side)

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
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


# class GroupViewList(generics.ListAPIView):
#     queryset = Group.objects.all()
#     serializer_class = GroupViewSerializer

class AddStudent(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = StudentSerializer

# Add assignment
# This is currently a ListCreateAPIView for debug purposes, will change to CreateAPIView
class AddAssignment(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
