
from django.contrib import admin
from django.urls import path, include

from main.views import login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('main/', include("main.urls")),
]
