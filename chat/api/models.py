from django.db import models

class Room(models.Model):
    question_text = models.CharField(max_length=200)
    admin= models.CharField(max_length=200)
    name= models.CharField(max_length=200)
    members= models.CharField(max_length=200)
    messages= models.CharField(max_length=200)
    backgroundColor= models.CharField(max_length=200)


class User(models.Model):
    name = models.CharField(max_length=200)
    avatar = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    owner =  models.ForeignKey(User, on_delete=models.CASCADE)
    text= models.CharField(max_length=200)