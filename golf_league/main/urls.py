from django.urls import path

from main.views import home, login

urlpatterns = [
    path('', home, name="home")
]
