from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('service/', views.service),
] + static(settings.MEDIA_URL,
           document_root=settings.MEDIA_ROOT)
