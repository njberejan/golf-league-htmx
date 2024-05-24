from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from django.views.generic import View

from main.forms import LoginForm

class LoginPageView(View):
    template_name = 'main/login.html'
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()
        message = ""
        return render(request, self.template_name, context={"form": form, "message": message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = "Login failed."
        return render(request, self.template_name, context={'form': form, 'message': message})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    return render(request, 'main/index.html')
