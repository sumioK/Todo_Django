from django.db import models

# Create your models here.

class TodoModel(models.Model):
  title = models.Charfield(max_length=100)
  memo = models.TextField()