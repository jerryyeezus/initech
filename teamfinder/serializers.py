__author__ = 'yee'
from rest_framework import serializers

from teamfinder.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('username', 'name', 'profile_img')
        # fields = ('id', 'name')

    def create(self, validated_data):
        return Student.objects.create(**validated_data) #TODO what is **

    def update(self, instance, validated_data):
        instance.title = validated_data.get('name', instance.name)
        instance.save()
        return instance
