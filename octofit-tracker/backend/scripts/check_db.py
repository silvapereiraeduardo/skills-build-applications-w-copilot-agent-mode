import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
django.setup()

from octofit_app.models import UserProfile, Activity


def check():
    ucount = UserProfile.objects.count()
    acount = Activity.objects.count()
    print(f'UserProfile count: {ucount}')
    print(f'Activity count: {acount}')
    for u in UserProfile.objects.all():
        acts = list(u.activities.all())
        print(f'- {u.username}: {len(acts)} activities')


if __name__ == '__main__':
    check()
