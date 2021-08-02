# from _typeshed import Self
from django.db import models

# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    age = models.IntegerField()
    def __repr__(self):
        return f"<users object : {self.first_name}, {self.last_name}, {self.email_address}, {self.age}, ({self.id})>"