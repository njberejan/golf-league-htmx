from django import forms
from django.contrib.auth.forms import UserCreationForm

from users.models import TeamManager

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)

class ESPNUserCreationForm(UserCreationForm):
    espn_id = forms.CharField(max_length=200)
    email = forms.EmailField()

    def save(self, commit=True):
        team_manager, _ = TeamManager.objects.get_or_create(espn_id=self.cleaned_data['espn_id'], email=self.cleaned_data["email"], username=self.cleaned_data['username'])
        team_manager.set_password(self.cleaned_data["password2"])
        if commit:
            team_manager.save()
        return team_manager
