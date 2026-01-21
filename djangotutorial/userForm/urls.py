from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_form_view, name='person_form'),
]
