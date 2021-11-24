from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category_name=models.CharField(null=True, max_length=20, unique=True)
    def __str__(self):
        return self.category_name

class Rooms(models.Model):
    room_name=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    price=models.FloatField(default=0)

    def __str__(self):
        return self.room_name

class BookRoom(models.Model):
    email=models.EmailField(max_length=50, null=False)
    phone_number=models.CharField(max_length=20, null=True)
    rooms=models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    check_in=models.DateTimeField(null=True)
    check_out = models.DateTimeField(null=True)
    going_to_destination=models.CharField(max_length=100, null=True)
    guest_quantity=models.IntegerField(default=0)

    @property
    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=True)
    address=models.CharField(max_length=100, null=True)
    email = models.EmailField(max_length=50, null=False)
    message=models.TextField(max_length=500, null=True)

    @property
    def full_name(self):
        return self.user.first_name + ' ' + self.user.last_name
