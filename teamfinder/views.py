from django.http import Http404
from django.shortcuts import render
import json

# Create your views here.
from rest_framework import generics, filters
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions, views, viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from teamfinder.models import Group, User, Course
from teamfinder.serializers import GroupViewSerializer, StudentSerializer, GroupAddSerializer, ProfessorAccountSerializer, CourseAddSerializer

# Return list for a given professor
class CourseAdd(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseAddSerializer

class CourseList(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseAddSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('course_professor', )
    # Retrieve, update or delete a snippet instance.
    # """
    # def get_object(self, pk):
    #     try:
    #         return Course.objects.filter(course_professor=pk)
    #     except Course.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk, format=None):
    #     courses = self.get_object(pk)
    #     serializer = CourseAddSerializer(courses)
    #     asdf = serializer.data
    #     return Response(serializer.data)


class StudentList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = StudentSerializer


class GroupAdd(APIView):
    def post(self, request):
        serializer = GroupAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfessorAccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'email'
    queryset = User.objects.all()
    serializer_class = ProfessorAccountSerializer

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

        serializer = ProfessorAccountSerializer(queryset, many=True)
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


class ProfessorLoginView(views.APIView):
    def post(self, request, format=None):
        email = request.data.get('email')
        password = request.data.get('password')

        account = authenticate(email=email, password=password)

        if account is not None:
            if account.is_active:
                login(request, account)

                serialized = ProfessorAccountSerializer(account)

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


class GroupViewList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupViewSerializer

