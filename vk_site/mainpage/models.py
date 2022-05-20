from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ListOfUsersModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    link = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.user} - {self.link}'
