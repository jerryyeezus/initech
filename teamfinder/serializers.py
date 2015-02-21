from rest_framework.views import APIView

__author__ = 'yee'
from rest_framework import serializers

from teamfinder.models import *

class ThingSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Thing.objects.create(**validated_data)

    class Meta:
        model = Thing
        fields = ('name')


class UserAccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    skills_str = serializers.CharField(write_only=True, required=False, allow_blank=True)
    skills = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('name', 'email', 'user_type', 'dept', 'password', 'confirm_password', 'gpa', 'bio', 'project_pref',
                  'skills', 'interests', 'linkedin', 'github', 'profile_img', 'skills_str')

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

        # def update(self, instance, validated_data):
        # instance.title = validated_data.get('name', instance.name)
        #     instance.save()
        #     return instance


# class GroupViewSerializer(serializers.ModelSerializer):
# class Meta:
#         model = Group

class CourseSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    class Meta:
        model = Course
        fields = ('csv_import', 'course_dept_and_id', 'course_name', 'course_professor', 'students', 'pk')

class GroupSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    class Meta:
        model = Group
        fields = ('pk', 'name', 'number', 'members', 'description')


class AssignmentSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        return Assignment.objects.create(**validated_data)

    class Meta:
        model = Assignment
        fields = ('pk', 'course_fk', 'assignment_number', 'assignment_title', 'assignment_text', 'groups')

# class GroupAddSerializer(serializers.ModelSerializer):
#     owner = serializers.CharField(required=True)
#
#     def create(self, validated_data):
#         group_owner = User.objects.get(pk=self.data.get('owner'))
#         validated_data['owner'] = group_owner
#
#         return Group.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('name', instance.name)
#         instance.save()
#         return instance
#
#     class Meta:
#         model = Group
#         fields = ('name', 'description', 'owner')
