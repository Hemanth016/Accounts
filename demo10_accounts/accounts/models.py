from django.db import models

class User(models.Model):
    name=models.CharField(max_length=30)
    password=models.IntegerField()
    email=models.EmailField(max_length=30)
    phoneno=models.IntegerField(max_length=30)

    def __str__(self):
        return self.name
