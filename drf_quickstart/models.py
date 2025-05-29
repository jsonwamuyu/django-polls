from django.db import models

class Course(models.Model):
    course_title = models.CharField(max_length=200)