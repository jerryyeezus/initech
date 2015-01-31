from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from teamfinder.models import Student, Group
from teamfinder.serializers import GroupViewSerializer, StudentSerializer, GroupAddSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class GroupAdd(APIView):
    def post(self, request):
        serializer = GroupAddSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GroupViewList(generics.ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupViewSerializer

