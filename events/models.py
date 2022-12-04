from django.db import models

# Create your models here.


class Role(models.Model):
    role = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.role


class User(models.Model):
    name = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    user = models.CharField(max_length=30)
    password = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    birthDate = models.DateField(auto_created=False)
    roleId = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class EventPlanner(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    photo = models.ImageField(null=True, blank=True, upload_to='eventPlanner/')
    ruc = models.CharField(max_length=11)
    userId = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self) -> str:
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=80)
    photo = models.ImageField(null=True, blank=True, upload_to='event/')
    description = models.TextField()
    dateEvent = models.DateField(
        auto_now_add=False, auto_now=False, blank=True)
    price = models.CharField(max_length=10)
    categoryId = models.ForeignKey(Category, on_delete=models.CASCADE)
    eventPlannerId = models.ForeignKey(EventPlanner, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
