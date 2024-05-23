from django.db import models

class Player(models.Model):
    class Position(models.TextChoices):
        QB = 'qb', 'Quarter Back'
        RB = 'rb', 'Running Back'
        WR = 'wr', 'Wide Receiver'
        TE = 'te', 'Tight End'
        K = 'k', 'Kicker'

    name = models.CharField(max_length=200, null=False, blank=False)
    roster = models.OneToOneField("teams.Roster", null=True, blank=True, on_delete=models.CASCADE)
    position = models.CharField(max_length=100, choices=Position.choices, blank=True, null=True)
    bye_week = models.PositiveIntegerField()

class DefenseST(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    roster = models.OneToOneField("teams.Roster", null=True, blank=True, on_delete=models.CASCADE)
