from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('educators/', views.educators, name='educators'),
    path('honors/', views.honors, name='honors'),
    path('gallery/', views.gallery, name='gallery'),
    path('videos/', views.videos, name='videos'),
    path('contact/', views.contact, name='contact'),
]