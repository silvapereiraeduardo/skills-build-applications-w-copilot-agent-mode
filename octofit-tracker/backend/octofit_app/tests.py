from django.test import TestCase
from .models import UserProfile, Activity


class ModelsTest(TestCase):
    def test_user_and_activity_creation(self):
        user = UserProfile.objects.create(username='testuser', email='test@example.com')
        act = Activity.objects.create(user=user, name='Run', duration_minutes=30, calories=300)
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(act.user.username, 'testuser')


class ExtendedModelsTest(TestCase):
    def test_team_workout_leaderboard(self):
        u1 = UserProfile.objects.create(username='u1')
        u2 = UserProfile.objects.create(username='u2')
        from .models import Team, Workout, LeaderboardEntry

        team = Team.objects.create(name='Team A')
        team.members.set([u1, u2])

        w = Workout.objects.create(user=u1, title='Morning', duration_minutes=20)

        le = LeaderboardEntry.objects.create(user=u1, points=100)

        self.assertEqual(Team.objects.count(), 1)
        self.assertEqual(Workout.objects.count(), 1)
        self.assertEqual(LeaderboardEntry.objects.count(), 1)
