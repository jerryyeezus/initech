from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class ProfessorAccountManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('No email supplied')

        account = self.model(
            email=self.normalize_email(email),
        )

        account.set_password(password)
        account.save()

        return account

class Professor(AbstractBaseUser):
    email = models.EmailField(primary_key=True, unique=True)
    dept = models.CharField(max_length=8, blank=False)

    objects = ProfessorAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'dept']

    def __unicode__(self):
        return self.email + ' ' + self.dept

class Student(AbstractBaseUser):
    def profile_file(self, filename):
        return 'static/' + str(self.name.replace(' ', '_')) + '_' + filename

    # TODO CHange
    objects = ProfessorAccountManager()

    # Linkedin
    linkedin = models.URLField()

    # Github
    github = models.URLField()

    # Project Preference (ordered list)

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

    # Email
    email = models.EmailField(primary_key=True, unique=True)
    def __unicode__(self):
        return self.email

class Course(models.Model):
    # Dept
    course_dept = models.TextField(blank=False)

    # Course ID
    course_id = models.IntegerField(blank=False)

    # Course CRM
    course_crm = str(course_dept) + ' ' + str(course_id)

    # Course name
    course_name = models.CharField(blank=False, max_length=64)

    # Professor
    course_professor = models.ForeignKey(Professor)

class Project(models.Model):
    # Category (Fill in via clustering methods)
    category = models.TextField(blank=False)

    # Description
    description = models.TextField(blank=False)

    # TODO Tags?
    # tags = ...

class Group(models.Model):
    # Primary key id
    group_id = models.AutoField(primary_key=True)

    # Group name
    name = models.CharField(max_length=24, blank=False)

    # Student owner
    owner = models.ForeignKey(Student, to_field='email', related_name='groups')

    # Description
    # For example, "Hi, we looking to do web development on blah..."
    # This is for introductory purpose, probably not going to use in algorithms
    description = models.TextField(blank=True)

    # Open roles TODO not sure how to represent this. Make table called Roles??

    class Meta:
        ordering = ['name']




# Student enrollment in class
class Enrollment(models.Model):
    user = models.ForeignKey(Student)
    course = models.ForeignKey(Course)

# Teacher for class
class Teaches(models.Model):
    professor = models.ForeignKey(Professor)
    course = models.ForeignKey(Course)

# Member of group
class Membership(models.Model):
    member = models.ForeignKey(Student)
    course = models.ForeignKey(Course)
    group = models.ForeignKey(Group)
    role = models.CharField(max_length=16)  # owner/tentative/confirmed
