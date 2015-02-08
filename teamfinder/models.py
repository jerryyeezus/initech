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

    # Linkedin
    linkedin = models.URLField()

    # Github
    github = models.URLField()

    # Project Preference (ordered list)
    # TODO

    # Biography
    bio = models.TextField()

    # Resume TODO
    # resume = models.FileField(upload_to=resume_file)

    # Peer Evaluation Score TODO
    # score = ...

    # Interests (AI, Web Development, Machine Learning, Databases, etc...) TODO
    # interests = ...

    # Full name
    name = models.TextField(max_length=100, blank=False)

    # Image URL
    profile_img = models.FileField(upload_to=profile_file, blank=True)

    def __unicode__(self):
        return self.type_and_email

class Course(models.Model):
    # Dept
    course_dept = models.TextField(blank=False)

    # Course ID
    course_id = models.IntegerField(blank=False)

    # Course name
    course_name = models.CharField(blank=False, max_length=64)

    # Professor
    course_professor = models.ForeignKey(User)

    # Import
    csv_import = models.FileField(upload_to='static', blank=True, null=True)

    # Students
    students = models.ManyToManyField(User, null=True, blank=True, related_name='students')

class Project(models.Model):
    # Category (Fill in via clustering methods)
    category = models.TextField(blank=False)

    # Description
    description = models.TextField(blank=False)

    # TODO Tags?
    # tags = ...

# class Group(models.Model):
#     # Primary key id
#     group_id = models.AutoField(primary_key=True)
#
#     # Group name
#     name = models.CharField(max_length=24, blank=False)
#
#     # Student owner
#     owner = models.ForeignKey(User, to_field='email', related_name='groups')
#
#     # Description
#     # For example, "Hi, we looking to do web development on blah..."
#     # This is for introductory purpose, probably not going to use in algorithms
#     description = models.TextField(blank=True)
#
#     # Open roles TODO not sure how to represent this. Make table called Roles??
#
#     class Meta:
#         ordering = ['name']

