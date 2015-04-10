from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

INSTRUCTOR = 'INSTRUCTOR'
STUDENT = 'STUDENT'
PLACEHOLDER = 'PLACEHOLDER'


class AccountManager(BaseUserManager):
    def create_user(self, email, user_type, name='', password=None, **kwargs):
        if not email:
            raise ValueError('No email supplied')

        account = self.model(
            email=self.normalize_email(email),
            user_type=user_type,
            type_and_email=user_type + '|' + email,
        )

        account.name = name
        account.set_password(password)
        account.save()
        return account

    def update(self, instance, validated_data):
        print 'update serializer'
        # instance.username = validated_data.get('username', instance.username)
        pass

# A skill can be language or concept
# Django, Javascript, REST, Machine Learning
class Thing(models.Model):
    name = models.CharField(unique=True, max_length=24)

    def __unicode__(self):
        return self.name

class User(AbstractBaseUser):
    USER_TYPE_CHOICES = (
        (INSTRUCTOR, 'INSTRUCTOR'),
        (PLACEHOLDER, 'PLACEHOLDER'),
        (STUDENT, 'STUDENT')
    )

    email = models.EmailField(unique=False)
    user_type = models.CharField(max_length=24, blank=False, choices=USER_TYPE_CHOICES)
    dept = models.CharField(max_length=8, blank=True)
    type_and_email = models.CharField(primary_key=True, max_length=64, unique=True)
    objects = AccountManager()
    skills_str = models.CharField(max_length=256, unique=False, blank=True)
    score = models.FloatField(blank=True, null=True)

    USERNAME_FIELD = 'type_and_email'
    REQUIRED_FIELDS = ['username', 'user_type']

    def profile_file(self, filename):
        return 'static/' + str(self.name.replace(' ', '_')) + '_' + filename

    '''
    Student fields
    '''

    # Full name
    name = models.TextField(max_length=100, blank=False)

    # Project Preference (ordered list)
    project_pref = models.ManyToManyField('Project', null=True)

    # Biography
    bio = models.TextField(blank=True)

    # GPA / 4.0
    gpa = models.FloatField(null=True)

    # Linkedin
    linkedin = models.URLField(blank=True)

    # Github
    github = models.URLField(blank=True)

    # skills (AI, Web Development, Machine Learning, Databases, etc...)
    # Used to match with project and group needs
    skills = models.ManyToManyField(Thing, related_name='skills', blank=True, null=True)

    # Used to match with project theme
    interests = models.ManyToManyField(Thing, related_name='interests', blank=True, null=True)

    # Image URL
    profile_img = models.FileField(upload_to=profile_file, blank=True, null=True)

    def __unicode__(self):
        return self.type_and_email

class Course(models.Model):
    # Course pk
    course_dept_and_id = models.TextField()

    # Course name
    course_name = models.CharField(blank=False, max_length=64)

    # Professor
    course_professor = models.ForeignKey(User)

    # Import
    csv_import = models.FileField(upload_to='static', blank=True, null=True)

    # Students
    students = models.ManyToManyField(User, null=True, blank=True, related_name='students')

    # Same teams disallowed across different assignments
    same_disallowed = models.BooleanField(blank=True, default=False)

    def __unicode__(self):
        return self.course_dept_and_id

class Project(models.Model):
    # Name
    name = models.CharField(max_length=24)

    # Category (Fill in via clustering methods)
    # category = models.ForeignKey('Thing', related_name='category', blank=True)
    category = models.CharField(max_length=24, blank=True)

    # Description
    description = models.TextField(blank=False)

    # FK to assignment
    ass_fk = models.ForeignKey('Assignment')

    # Tags
    tags = models.ManyToManyField(Thing)

class Team(models.Model):
    # Group name
    name = models.CharField(max_length=24, blank=False)

    # Group #
    number = models.IntegerField(blank=False)

    # Members
    members = models.ManyToManyField(User, null=True, blank=True, related_name='members')

    # Description
    # For example, "Hi, we looking to do web development on blah..."
    description = models.TextField(blank=True)

    lfm = models.BooleanField(blank=True, default=False)

    score = models.FloatField(null=True, blank=True)
    # TODO skills needed?
    def __unicode__(self):
        return self.name

# class TeamRecommendation(models.Model):
#     team_fk = models.ForeignKey(Team)
#     compat_score = models.IntegerField()

class JoinRequest(models.Model):
    requester = models.ForeignKey(User)
    message = models.CharField(max_length=64, blank=True)
    team = models.ForeignKey(Team)

class Assignment(models.Model):
    # Course
    course_fk = models.ForeignKey(Course)

    # Number
    assignment_number = models.IntegerField()

    # Title
    assignment_title = models.CharField(max_length=24, blank=True)

    # Description
    assignment_text = models.CharField(max_length=800, blank=True)

    # Groups
    teams = models.ManyToManyField(Team, null=True, blank=True)


class Question(models.Model):
    ass_fk = models.ForeignKey(Assignment)
    text = models.CharField(max_length=48)
    lo = models.CharField(max_length=48)
    hi = models.CharField(max_length=48)
    type = models.CharField(max_length=48, blank=True)
    def __unicode__(self):
        return self.text

# class Project(models.Model):
#     ass_fk = models.ForeignKey(Assignment)
#     name = models.CharField(max_length=24)
#     description = models.TextField(blank=False)


class Answer(models.Model):
    question_fk = models.ForeignKey(Question)
    user_fk = models.ForeignKey(User)
    value = models.IntegerField()
    weight = models.FloatField()
    class Meta:
        unique_together = (('user_fk', 'question_fk'), )

class Notification(models.Model):
    message = models.TextField(blank=True)
    from_user = models.ForeignKey(User, related_name='from_user')
    to_user = models.ForeignKey(User, related_name='to_user')

class LFG(models.Model):
    user_fk = models.ForeignKey(User, related_name='user_fk')
    ass_fk = models.ForeignKey(Assignment)
    class Meta:
        unique_together = (('user_fk', 'ass_fk'), )

# class LFM(models.Model):
#     team_fk = models.ForeignKey(Team, related_name='team_fk')
#     ass_fk = models.ForeignKey(Assignment)
