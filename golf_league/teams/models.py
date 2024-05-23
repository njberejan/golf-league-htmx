from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey

from league.models import League
from schedule.models import LeagueWeek
from users.models import TeamManager

class LineUp(models.Model):
    league_week = models.OneToOneField(LeagueWeek, null=False, blank=False, on_delete=models.PROTECT)
    locked = models.BooleanField(default=False)
    qb = models.OneToOneField("players.Player", null=True, blank=True, related_name='qb_lineup', on_delete=models.PROTECT)
    rb = models.OneToOneField("players.Player", null=True, blank=True, related_name='rb_lineup', on_delete=models.PROTECT)
    wr = models.ForeignKey("players.Player", null=True, blank=True, related_name='wr_set', on_delete=models.PROTECT)
    te = models.OneToOneField("players.Player", null=True, blank=True, related_name='te_lineup', on_delete=models.PROTECT)
    flex = models.OneToOneField("players.Player", null=True, blank=True, related_name='flex_lineup', on_delete=models.PROTECT)
    dst = models.OneToOneField("players.DefenseST", null=True, blank=True, related_name='dst_lineup', on_delete=models.PROTECT)
    k = models.OneToOneField("players.Player", null=True, blank=True, related_name='k_lineup', on_delete=models.PROTECT)

class Roster(models.Model):
    lineup = models.OneToOneField(LineUp, null=True, blank=True, on_delete=models.PROTECT)

class Team(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    espn_id = models.CharField(max_length=200, null=False, blank=False)
    roster = models.OneToOneField(Roster, null=True, blank=True, on_delete=models.CASCADE)
    league = models.ForeignKey(League, on_delete=models.CASCADE, null=False, blank=False)
    manager = models.OneToOneField(TeamManager, on_delete=models.CASCADE, null=False, blank=False)
