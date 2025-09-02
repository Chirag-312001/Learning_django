from django.urls import path
from . import views   # <-- make sure this is correct

urlpatterns = [
    path('', views.home, name='home'),
]
