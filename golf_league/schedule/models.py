from django.db import models

from stats import models as stats_models

class LeagueWeek(models.Model):
    week_number = models.PositiveIntegerField()

class LeagueSeason(models.Model):
    season_year = models.PositiveIntegerField()

class PlayerWeek(models.Model):
    player = models.ForeignKey("players.Player", on_delete=models.CASCADE, null=False, blank=False)
    week_number = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    projected_stats = models.OneToOneField(stats_models.PlayerStats, on_delete=models.CASCADE, null=True, blank=True, related_name="player_projected_stats")
    actual_stats = models.OneToOneField(stats_models.PlayerStats, on_delete=models.CASCADE, null=True, blank=True, related_name="player_actual_stats")

class DefenseSTWeek(models.Model):
    defense = models.ForeignKey("players.DefenseST", on_delete=models.CASCADE, null=False, blank=False)
    week_number = models.PositiveIntegerField()
    start_time = models.DateTimeField()
    projected_stats = models.OneToOneField(stats_models.DefenseSTStats, on_delete=models.CASCADE, null=True, blank=True, related_name="defensest_projected_stats")
    actual_stats = models.OneToOneField(stats_models.DefenseSTStats, on_delete=models.CASCADE, null=True, blank=True, related_name="defensest_actual_stats")
