from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password

from django.views.generic import View

from main.forms import LoginForm, ESPNUserCreationForm
from users.models import TeamManager

class UserCreationPageView(View):
    template_name = 'main/user_creation.html'
    form_class = ESPNUserCreationForm

    def get(self, request):
        form = self.form_class()
        message = ""
        return render(request, self.template_name, context={"form": form, "message": message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
        else:
            message = "User creation failed."
        return render(request, self.template_name, context={"form": form, "message": message})

class LoginPageView(View):
    template_name = 'main/login.html'
    form_class = LoginForm

    def authenticate(self, username, password):
        try:
            team_manager = TeamManager.objects.get(username=username)
            if check_password(password, team_manager.password):
                return team_manager
            else:
                return None
        except TeamManager.DoesNotExist:
            return None

    def get(self, request):
        form = self.form_class()
        message = ""
        return render(request, self.template_name, context={"form": form, "message": message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = self.authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = "Login failed."
        return render(request, self.template_name, context={'form': form, 'message': message})

@login_required
def home(request):
    return render(request, 'main/index.html')
