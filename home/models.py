from turtle import title
from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="question")
    body = models.TextField()
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.title[:20]}"

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="answer")
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name="answer") 
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.question} - {self.body[0:20]}"
