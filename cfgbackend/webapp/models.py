from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.TextField()
    description=models.TextField()
    no_of_students=models.IntegerField(default=0)
    Course_creation=models.DateField()
    Validity=models.IntegerField()
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.username
                             
class users(models.Model):
    name=models.CharField(max_length=10)
    role=models.CharField(max_length=10)
    username=models.CharField(max_length=10)
    email=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    organisation=models.CharField(max_length=20)
    courseID=models.CharField(max_length=20)
    courseName=models.CharField(max_length=20)

    def __str__(self):
        return self.username

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name=models.TextField()
    description=models.TextField()
    no_of_students=models.IntegerField(default=0)
    Course_creation=models.DateField()
    Validity=models.IntegerField()
    user = models.ForeignKey(User, editable=False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name



