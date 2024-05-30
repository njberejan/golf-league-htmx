import uuid
from django.db import models
from django.contrib.auth.models import User

class TeamManager(User):
    espn_id = models.CharField(max_length=200, null=False, blank=False, unique=True)
