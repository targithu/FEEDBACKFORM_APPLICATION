from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    subject = models.CharField(max_length=40)
    email = models.EmailField()
    comments = models.TextField()
    RATING_CHOICES = [
        (1, '1⭐'),
        (2, '2⭐'),
        (3, '3⭐'),
        (4, '4⭐'),
        (5, '5⭐'),
    ]
    rating = models.IntegerField(default=3,choices=RATING_CHOICES)

    def __str__(self):
        return f"{self.subject} {self.email} {self.comments} {self.rating}"
