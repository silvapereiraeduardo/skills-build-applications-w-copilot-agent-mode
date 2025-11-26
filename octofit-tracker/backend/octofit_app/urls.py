from rest_framework import routers
from .views import (
    UserProfileViewSet,
    ActivityViewSet,
    TeamViewSet,
    WorkoutViewSet,
    LeaderboardEntryViewSet,
    api_root,
)
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'users', UserProfileViewSet, basename='userprofile')
router.register(r'activities', ActivityViewSet, basename='activity')
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'workouts', WorkoutViewSet, basename='workout')
router.register(r'leaderboard', LeaderboardEntryViewSet, basename='leaderboardentry')

urlpatterns = [
    path('', api_root, name='api-root'),
    path('v1/', include(router.urls)),
]
