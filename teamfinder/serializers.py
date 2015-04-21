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


class StudentRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'email', 'user_type', 'dept', 'gpa', 'bio', 'project_pref',
                  'interests', 'linkedin', 'github', 'profile_img', 'score')


class UserAccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    confirm_password = serializers.CharField(write_only=True, required=True)
    # skills_str = serializers.CharField(write_only=True, required=False, allow_blank=True)
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


class CourseSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        return Course.objects.create(**validated_data)

    class Meta:
        model = Course
        fields = ('csv_import', 'course_dept_and_id', 'course_name', 'course_professor', 'students', 'pk')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('pk','name', 'description')


class TeamSerializer(serializers.ModelSerializer):
    members = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    project_pref = ProjectSerializer(many=True)

    def create(self, validated_data):
        return Team.objects.create(**validated_data)

    class Meta:
        model = Team
        fields = ('pk', 'name', 'number', 'members', 'description', 'lfm', 'project_pref', 'skills_needed')


class TeamRecommendationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('pk', 'name', 'number', 'members', 'description', 'lfm', 'score')


class JoinRequestSerializer(serializers.ModelSerializer):
    # members = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        return JoinRequest.objects.create(**validated_data)

    class Meta:
        model = JoinRequest
        fields = ('pk', 'requester', 'message', 'team')


class AssignmentSerializer(serializers.ModelSerializer):
    teams = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        return Assignment.objects.create(**validated_data)

    class Meta:
        model = Assignment
        fields = ('pk', 'course_fk', 'assignment_number', 'assignment_title', 'assignment_text', 'teams')


class AnswerSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Answer.objects.create(**validated_data)

    class Meta:
        model = Answer
        fields = ('question_fk', 'user_fk', 'value', 'weight')


class QuestionSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    class Meta:
        model = Question
        fields = ('pk', 'ass_fk', 'text', 'hi', 'lo')


# class LFMSerializer(serializers.ModelSerializer):
# def create(self, validated_data):
# return LFM.objects.create(**validated_data)
#
#     class Meta:
#         model = LFM
#         fields = ('team_fk', 'ass_fk')

class LFGSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return LFG.objects.create(**validated_data)

    class Meta:
        model = LFG
        fields = ('pk', 'user_fk', 'ass_fk')


class ProjectSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Project.objects.create(**validated_data)

    class Meta:
        model = Project
        fields = ('pk', 'ass_fk', 'name', 'description', 'category')


class NotificationSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        return Notification.objects.create(**validated_data)

    class Meta:
        model = Notification
        fields = ('pk', 'message', 'to_user', 'from_user')
