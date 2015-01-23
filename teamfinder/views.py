from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from teamfinder.models import Student
from teamfinder.serializers import StudentSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
