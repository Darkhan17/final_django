from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser


# Create your models here.



class User(AbstractUser):
    midle_name = models.CharField(max_length=200)
    user_permissions = AbstractUser.user_permissions
    groups = AbstractUser.groups


class BookJournalBase(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.CharField(max_length=500)
    created_at = models.DateField(auto_now_add=True)


class Book(BookJournalBase):
    num_pages = models.IntegerField()
    genre = models.CharField(max_length=500)



class Journal(BookJournalBase):
    type = models.CharField(max_length=200)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE, null=True)