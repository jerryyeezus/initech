from django.http import Http404
from django.shortcuts import render
import json

# Create your views here.
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import generics, filters
from django.contrib.auth import authenticate, login, logout
import StringIO
from rest_framework import permissions, views, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from teamfinder.models import User, Course
from teamfinder.serializers import StudentSerializer, UserAccountSerializer, CourseSerializer
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

# Return list for a given professor
class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('course_professor', )
    authentication_classes = (SessionAuthentication, BasicAuthentication)


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
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)
            return Response(
                serializer.validated_data, status=status.HTTP_201_CREATED
            )
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
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
