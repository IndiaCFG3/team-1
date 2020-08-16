from django.db import models

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