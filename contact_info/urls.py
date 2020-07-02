from django.urls import path
from contact_info import views

urlpatterns = [
    path('', views.contact_info, name = 'contact'),
]