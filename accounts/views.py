from dj_rest_auth.views import LogoutView
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

class CustomLogoutView(LogoutView):
    permission_classes = (IsAuthenticated,)

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer



