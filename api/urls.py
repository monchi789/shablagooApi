from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('roles', RoleViewSet, 'roles')
router.register('users', UserViewSet, 'users')
router.register('eventPlanners', EventPlannerViewSet, 'eventPlanners')
router.register('categorys', CategoryViewSet, 'categorys')
router.register('events', EventViewSet, 'events')

urlpatterns = [] + static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

urlpatterns += router.urls
