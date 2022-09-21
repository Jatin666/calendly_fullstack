from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'event', views.EventViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('main/', views.index, name='index')
]
 