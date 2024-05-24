
from django.contrib import admin
from django.urls import path, include

from main.views import logout_view, LoginPageView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginPageView.as_view(template_name="main/login.html"), name="login"),
    path('logout/', logout_view, name="logout"),
    path('main/', include("main.urls")),
]
