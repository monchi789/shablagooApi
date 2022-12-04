from django.urls import path, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from .api import *

router = routers.DefaultRouter()

router.register('roles/', RoleViewSet, 'roles')
router.register('users/', UserViewSet, 'users')
router.register('eventPlanners/', EventPlannerViewSet, 'eventPlanners')
router.register('categorys/', CategoryViewSet, 'categorys')
router.register('events/', EventViewSet, 'events')

urlpatterns = [
    re_path(r'^media/(?P<path>.*)$', serve, {
        'document_root': settings.MEDIA_ROOT,
    })
]

urlpatterns += router.urls
