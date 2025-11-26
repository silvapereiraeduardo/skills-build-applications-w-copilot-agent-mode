from rest_framework import serializers
from .models import UserProfile, Activity, Team, Workout, LeaderboardEntry


class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    activities = ActivitySerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ['id', 'username', 'email', 'created_at', 'activities']


class TeamSerializer(serializers.ModelSerializer):
    members = UserProfileSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ['id', 'name', 'members']


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'


class LeaderboardEntrySerializer(serializers.ModelSerializer):
    user = UserProfileSerializer(read_only=True)

    class Meta:
        model = LeaderboardEntry
        fields = ['id', 'user', 'points', 'updated_at']
