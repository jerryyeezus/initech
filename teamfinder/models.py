from django.db import models


class User(models.Model):
    def profile_file(self, filename):
        return 'static/' + str(self.pk) + '_' + filename

    # GT username
    username = models.TextField(max_length=64, primary_key=True, blank=False, unique=True)

    # Full name
    name = models.TextField(max_length=100, blank=False)

    # Image URL
    profile_img = models.FileField(upload_to=profile_file, blank=True)

    # Email
    email = models.EmailField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['username', 'name', 'profile_img']
        abstract = True

class Professor(User):
    dept = models.CharField(max_length=8, blank=False)

class Student(User):
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
    def __unicode__(self):
        return self.username

class Course(models.Model):
    # Dept
    course_dept = models.TextField(blank=False)

    # Course ID
    course_id = models.IntegerField(blank=False)

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
    owner = models.ForeignKey(Student, to_field='username', related_name='groups')

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
