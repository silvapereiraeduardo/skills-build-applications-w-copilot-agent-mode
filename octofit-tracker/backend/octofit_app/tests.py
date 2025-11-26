from django.test import TestCase
from .models import UserProfile, Activity


class ModelsTest(TestCase):
    def test_user_and_activity_creation(self):
        user = UserProfile.objects.create(username='testuser', email='test@example.com')
        act = Activity.objects.create(user=user, name='Run', duration_minutes=30, calories=300)
        self.assertEqual(UserProfile.objects.count(), 1)
        self.assertEqual(Activity.objects.count(), 1)
        self.assertEqual(act.user.username, 'testuser')
