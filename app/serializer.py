from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields="__all__"
class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rooms
        fields="__all__"
class BookRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model=BookRoom
        fields="__all__"
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model=Contact
        fields="__all__"

# register/login
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email"]
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password"]
        extra_kwargs={'password':{"write_only":True}}
    def create(self, validated_data):
        user=User.objects.create_user(
            validated_data["username"],
            validated_data["password"],
            validated_data["email"]
        )
        return user