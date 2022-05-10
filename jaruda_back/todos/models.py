from pyexpat import model
from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=100)
    create_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.task
