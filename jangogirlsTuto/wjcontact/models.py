from django.db import models
from django.utils import timezone

# Create your models here.
class WJContact(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    e_mail_address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    detail = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.name