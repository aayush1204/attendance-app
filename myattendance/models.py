from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.

# class User(models.Model):
#     student_name = models.CharField(max_length=250,null=True)

#     def __str__(self):
#         return self.student_name

class StudentEntries(models.Model):
    student_name = models.ForeignKey(User , on_delete=models.CASCADE, null=True)
    subject_name = models.CharField(max_length=250,null=True)
    total_lectures = models.IntegerField(default=0)
    attended_lectures = models.IntegerField(default=0)
    missed_lectures = models.IntegerField(default=0)
    idn= models.IntegerField(default=0)
    percentage = models.FloatField(default=0)

    def __str__(self):
            return self.subject_name

