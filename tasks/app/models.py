from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Feedback(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    Comments=models.TextField()
    def __str__(self):
        return  f"{self.name} {self.email} {self.Comments}"