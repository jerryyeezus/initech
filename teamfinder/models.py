from random import randint
from django.db import models

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=100, blank=False)

    class Meta:
        ordering = ['name']

def mugshot_file(instance, filename):
    return '/'.join(['profiles', str(instance.pk), filename])

class Student(models.Model):
    username = models.TextField(max_length=64, primary_key=True)
    name = models.TextField(max_length=100, blank=False)
    profile_img = models.FileField(upload_to=mugshot_file)
    committed_group_id = models.OneToOneField(Group, null=True)

    # Generate unique id
    def generate_id(self, MAX_STUDENTS=256, *args, **kwargs):
        rand_id = randint(0,MAX_STUDENTS)
        while Student.objects.filter(id=rand_id).exists():
            rand_id = randint(0,MAX_STUDENTS)

        return rand_id

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['username', 'name', 'profile_img', 'committed_group_id']


