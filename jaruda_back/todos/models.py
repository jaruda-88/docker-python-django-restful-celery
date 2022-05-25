from pyexpat import model
from turtle import Turtle
from django.db import models

# Create your models here.
class Todo(models.Model):
    dt_id = models.ForeignKey("DTType", related_name="DTType", db_column="dt_id", blank=True, null=True)
    task = models.CharField(max_length=100)
    expire_at = models.DateTimeField(default=None, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.task


class DTType(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self):
        return self.name
