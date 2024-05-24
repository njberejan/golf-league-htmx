from django.db import models
from django.contrib.auth.models import User

class TeamManager(models.Model):
    espn_id = models.CharField(max_length=200, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
