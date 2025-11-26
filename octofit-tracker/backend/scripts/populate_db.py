import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_app.models import UserProfile, Activity


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

    print('Populated octofit_db with test data')


if __name__ == '__main__':
    populate()
