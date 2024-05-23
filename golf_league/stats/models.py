from django.db import models

class PlayerStats(models.Model):
    points = models.FloatField()
    rushing_attempts = models.PositiveIntegerField()
    passing_attempts = models.PositiveIntegerField()
    receptions = models.PositiveIntegerField()
    field_goal_attempts = models.PositiveIntegerField()

class DefenseSTStats(models.Model):
    points = models.FloatField()
