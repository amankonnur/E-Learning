from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class PersonDetails(AbstractUser):
    designation_choices = [
        ('Student', 'student'), ('Teacher', 'teacher'), ('Admin', 'admin')
    ]
    designation = models.CharField(max_length=20,choices=designation_choices,default='Student')

    def __str__(self):
        return self.username + self.designation