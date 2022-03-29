from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import UserInitSerializer, UserFormSerializer
from .models import User


# Create APIView for `init`
class UserInitAPIView(viewsets.ModelViewSet):
    """After each correct entry will be generated several users with this data and  20 users with fake data"""
    queryset = User.objects.all()
    serializer_class = UserInitSerializer

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
