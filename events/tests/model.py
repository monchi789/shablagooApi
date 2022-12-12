from django.test import TestCase
from events.models import *

# Create your tests here.


class RoleTest(TestCase):

    def create_role(self, role="Creador"):
        return Role.objects.create(role=role)

    def test_role_creation(self):
        r = self.create_role()
        self.assertTrue(isinstance(r, Role))
        self.assertEqual(r.__str__(), r.role)


class UserTest(TestCase):

    r = Role.objects.create(role="Creador de Contenido")

    def create_user(self, name="Juan", lastName="Gonzales", user="Juan123", password="1234", phone="940675648", email="juan@gmail.com", birthDate="2001-02-01", roleId=r):
        return User.objects.create(name=name, lastName=lastName, user=user,
                                   password=password, phone=phone, email=email, birthDate=birthDate, roleId=roleId)

    def test_user_creation(self):
        u = self.create_user()
        self.assertTrue(isinstance(u, User))
        self.assertEqual(u.__str__(), u.name)


class EventPlannerTest(TestCase):

    r = Role.objects.create(role="Organizador")
    u = User.objects.create(name="Juan", lastName="Gonzales", user="Juan123", password="1234",
                            phone="940675648", email="juan@gmail.com", birthDate="2001-02-01", roleId=r)

    def create_eventPlanner(self, name="Esencia", location="Limacpampa", photo="/media/eventPlanner/thumb-1920-701031.png", ruc="98676787457", userId=u):
        return EventPlanner.objects.create(name=name, location=location, photo=photo, ruc=ruc, userId=userId)

    def test_eventPlanner_creation(self):
        ep = self.create_eventPlanner()
        self.assertTrue(isinstance(ep, EventPlanner))
        self.assertEqual(ep.__str__(), ep.name)


class CategoryTest(TestCase):

    def create_category(self, name="Cuentos", description="Es una funcion de cuentos infantiles"):
        return Category.objects.create(name=name, description=description)

    def test_category_creation(self):
        c = self.create_category()
        self.assertTrue(isinstance(c, Category))
        self.assertEqual(c.__str__(), c.name)


class EventTest(TestCase):

    r = Role.objects.create(role="Organizador")
    u = User.objects.create(name="Juan", lastName="Gonzales", user="Juan123", password="1234",
                            phone="940675648", email="juan@gmail.com", birthDate="2001-02-01", roleId=r)
    c = Category.objects.create(
        name="Cuentos", description="Es una funcion de cuentos infantiles")
    ep = EventPlanner.objects.create(name="Esencia", location="Limacpampa",
                                     photo="/media/eventPlanner/thumb-1920-701031.png", ruc="98676787457", userId=u)

    def create_event(self, name="Cuentos andinos", photo="/media/event/thumb-1920-701031.png", description="Es una presentacion de cuentos andinos a cargo de Julian un experto cuentero...", dateEvent="2001-02-01", price="15", categoryId=c, eventPlannerId=ep):

        return Event.objects.create(name=name, photo=photo, description=description, dateEvent=dateEvent, price=price, categoryId=categoryId, eventPlannerId=eventPlannerId)

    def test_event_creation(self):
        e = self.create_event()
        self.assertTrue(isinstance(e, Event))
        self.assertEqual(e.__str__(), e.name)
