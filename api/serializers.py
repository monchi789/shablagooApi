from rest_framework import serializers
from events.models import *


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ('id', 'role',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'lastName', 'user', 'password',
                  'phone', 'email', 'birthDate', 'roleId',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'description',)


class EventPlannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventPlanner
        fields = ('id', 'name', 'location', 'photo', 'ruc', 'userId',)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 'name', 'photo', 'description', 'dateEvent',
                  'price', 'categoryId', 'eventPlannerId',)
