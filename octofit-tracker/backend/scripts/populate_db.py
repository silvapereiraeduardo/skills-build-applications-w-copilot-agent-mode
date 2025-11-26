import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_app.models import UserProfile, Activity, Team, Workout, LeaderboardEntry


def populate():
    UserProfile.objects.all().delete()
    Activity.objects.all().delete()

    users = []
    for i in range(1, 6):
        u = UserProfile.objects.create(username=f'user{i}', email=f'user{i}@example.com')
        users.append(u)

    for u in users:
        Activity.objects.create(user=u, name='Run', duration_minutes=30, calories=250)
        Activity.objects.create(user=u, name='Bike', duration_minutes=45, calories=400)

    # Create a team and add first two users
    team = Team.objects.create(name='Alpha Team')
    team.members.set(users[:2])

    # Create workouts
    Workout.objects.create(user=users[0], title='Morning Run', duration_minutes=20)
    Workout.objects.create(user=users[1], title='Evening Ride', duration_minutes=45)

    # Leaderboard entries
    LeaderboardEntry.objects.create(user=users[0], points=150)
    LeaderboardEntry.objects.create(user=users[1], points=120)

    print('Populated octofit_db with test data')


if __name__ == '__main__':
    populate()
