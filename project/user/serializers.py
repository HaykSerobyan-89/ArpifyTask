from rest_framework import serializers
from .models import User


# Create  `init` serializer
class UserInitSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'dob', 'name', 'last_name', 'gender')


# Create  `form` serializer
class UserFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('dob', 'name', 'last_name', 'gender', 'cv', 'image')