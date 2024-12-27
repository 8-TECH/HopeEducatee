from django.urls import path
from . import views

urlpatterns = [
    path('', views.school_view, name='school')  # Updated function name to 'school_view'
]
