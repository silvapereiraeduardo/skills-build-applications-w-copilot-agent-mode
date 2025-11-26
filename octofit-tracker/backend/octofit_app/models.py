from django.db import models
from bson import ObjectId


def generate_objectid():
    return str(ObjectId())


class UserProfile(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=generate_objectid)
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username


class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=generate_objectid)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    name = models.CharField(max_length=200)
    duration_minutes = models.IntegerField()
    calories = models.IntegerField(default=0)
    logged_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.user})"


class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=generate_objectid)
    name = models.CharField(max_length=200, unique=True)
    members = models.ManyToManyField(UserProfile, related_name='teams')

    def __str__(self):
        return self.name


class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=generate_objectid)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='workouts')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    duration_minutes = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.user})"


class LeaderboardEntry(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=generate_objectid)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='leaderboard_entries')
    points = models.IntegerField(default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-points']

    def __str__(self):
        return f"{self.user.username}: {self.points}"
