# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Attendence(models.Model):
    student_name = models.CharField(max_length=250)
    student_id = models.CharField(max_length=400)

class Course(models.Model):
    course = models.ForeignKey(Attendence, on_delete=models.CASCADE)