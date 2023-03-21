from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Contact(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email = models.EmailField()
    phone_number = models.IntegerField(null=True)
    Address = models.TextField()
    
    def __str__(self):
        return self.name