from events.models import *
from rest_framework import viewsets, permissions
from .serializers import *


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RoleSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer


class EventPlannerViewSet(viewsets.ModelViewSet):
    queryset = EventPlanner.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EventPlannerSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = EventSerializer
