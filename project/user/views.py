from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserInitSerializer, UserFormSerializer
from .models import User
from faker import Faker
import numpy as np


# Create APIView for `init`
class UserInitAPIView(viewsets.ModelViewSet):
    """After each correct entry will be generated several users with this data and  20 users with fake data"""
    queryset = User.objects.all()
    serializer_class = UserInitSerializer

    def get_success_headers(self, data):
        # Creating users with posted data
        for _ in range(5):
            User.objects.create(
                dob=data['dob'],
                name=data['name'],
                last_name=data['last_name'],
                gender=data['gender'],
            )

        ''' Creating 30 fake users, 
        after which some users may not pass validation 
        and not be included in the database'''
        for _ in range(30):
            fake = Faker()
            User.objects.create(
                dob=fake.date_of_birth(),
                name=fake.first_name(),
                last_name=fake.last_name(),
                gender=np.random.choice(["m", "f"]),
            )

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        r = User.objects.all().values('id', 'dob', 'name', 'last_name', 'gender')
        return Response(r, status=status.HTTP_201_CREATED, headers=headers)


# Create APIView for `form`
class UserFormAPIView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserFormSerializer
