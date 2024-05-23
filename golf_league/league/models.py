from django.db import models

from users.models import TeamManager

class Schedule(models.Model):
    pass

class League(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    commissioner = models.ForeignKey(TeamManager, on_delete=models.CASCADE, null=False, blank=False)
    league_id = models.PositiveIntegerField(null=False, blank=False)
    current_season = models.PositiveIntegerField(null=True, blank=True)
    current_schedule = models.OneToOneField(Schedule, on_delete=models.CASCADE, null=True, blank=True)
