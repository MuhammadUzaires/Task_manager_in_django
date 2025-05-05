from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    Status_Choices=(
        ("todo","To Do"),
        ("in_progress","In Progress"),
        ("done","Done")
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    status=models.CharField(max_length=20,choices=Status_Choices,default="todo")
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title