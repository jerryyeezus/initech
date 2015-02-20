from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

INSTRUCTOR = 'INSTRUCTOR'
STUDENT = 'STUDENT'
PLACEHOLDER = 'PLACEHOLDER'


class AccountManager(BaseUserManager):
    def create_user(self, email, user_type, password=None, **kwargs):
        if not email:
            raise ValueError('No email supplied')

        account = self.model(
            email=self.normalize_email(email),
            user_type=user_type,
            type_and_email=user_type + '|' + email
        )

        account.set_password(password)
        account.save()

        return account

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
    project_pref = models.ManyToManyField('Project')

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

    # Same

    def __unicode__(self):
        return self.course_dept_and_id

class Project(models.Model):
    # Name
    name = models.CharField(max_length=24)

    # Category (Fill in via clustering methods)
    category = models.ForeignKey('Thing', related_name='category')

    # Description
    description = models.TextField(blank=False)

    # FK to assignment
    assignment_fk = models.ForeignKey('Assignment')

    # Tags
    tags = models.ManyToManyField(Thing)

class Group(models.Model):
    # Group name
    name = models.CharField(max_length=24, blank=False)

    # Creator
    owner = models.ForeignKey(User)

    # Members
    members = models.ManyToManyField(User, null=True, blank=True, related_name='members')

    # Description
    # For example, "Hi, we looking to do web development on blah..."
    description = models.TextField(blank=True)

    # TODO skills needed?

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
    groups = models.ManyToManyField(Group, null=True, blank=True)
