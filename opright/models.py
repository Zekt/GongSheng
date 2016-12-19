from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()

class Participant(models.Model):
    name = models.CharField(max_length=30)
    join_date = models.DateTimeField()
    score = models.IntegerField()
    task = models.ManyToManyField(Task)
    avatar = models.ImageField()

class Posts(models.Model):
    post_id = models.CharField(max_length=50)
    post_date = models.DateTimeField()
    post_creator = models.ForeignKey(Participant)
    post_task = models.ForeignKey(Task)
    post_comfirmed = models.NullBooleanField()
