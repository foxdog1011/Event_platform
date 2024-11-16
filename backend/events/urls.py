from django.urls import path, include
from . import views
from rest_framework import routers
from .views import EventViewSet 

router = routers.DefaultRouter()
router.register(r'events', EventViewSet)  

urlpatterns = [
    path('', views.event_list, name='event_list'),
    path('event/new/', views.event_create, name='event_create'),
    path('event/<int:pk>/edit/', views.event_edit, name='event_edit'),
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),
    path('event/<int:pk>/registrations/', views.event_registrations, name='event_registrations'),
    path('api/', include(router.urls)),
]
