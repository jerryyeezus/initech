from rest_framework.views import APIView

__author__ = 'yee'
from rest_framework import serializers

from teamfinder.models import *

class UserAccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('email', 'user_type', 'dept', 'password', 'confirm_password')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        password = validated_data.get('password', None)
        confirm_password = validated_data.get('confirm_password', None)

        if password == confirm_password:
            instance.set_password(password)
            instance.save()
            # update_session_auth_hash(self.context.get('request'), instance)

        return instance


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'name', 'profile_img')

    def create(self, validated_data):
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('name', instance.name)
        instance.save()
        return instance

class GroupViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group

class CourseSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        course_professor = User.objects.get(pk=self.data.get('course_professor'))
        validated_data['course_professor'] = course_professor
        return Course.objects.create(**validated_data)
    class Meta:
        model = Course
        fields = ('course_dept', 'course_id', 'course_name', 'course_professor')

class GroupAddSerializer(serializers.ModelSerializer):
    owner = serializers.CharField(required=True)

    def create(self, validated_data):
        group_owner = User.objects.get(pk=self.data.get('owner'))
        validated_data['owner'] = group_owner

        return Group.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = Group
        fields = ('name', 'description', 'owner')
