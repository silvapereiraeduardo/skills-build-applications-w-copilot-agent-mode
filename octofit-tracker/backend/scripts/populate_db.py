"""
Populate the octofit_db database with test data.

This script creates the following collections with test documents:
- users
- activities
- teams
- workouts
- leaderboard

It uses pymongo to insert documents and also attempts to create Django ORM
objects so `djongo`-backed ORM queries can see the test data.
"""

from pymongo import MongoClient
import os


def populate(uri=None, dbname='octofit_db'):
    uri = uri or os.environ.get('MONGO_URI', 'mongodb://127.0.0.1:27017')
    client = MongoClient(uri)
    db = client[dbname]

    # Clear existing collections
    for coll in ['users', 'activities', 'teams', 'workouts', 'leaderboard']:
        if coll in db.list_collection_names():
            db.drop_collection(coll)

    # Insert users using insert_many
    user_docs = [{'username': f'user{i}', 'email': f'user{i}@example.com'} for i in range(1, 6)]
    result = db.users.insert_many(user_docs)
    users = result.inserted_ids

    # Insert activities (2 per user) using insert_many
    activity_docs = []
    for uid in users:
        activity_docs.append({'user_id': uid, 'name': 'Run', 'duration_minutes': 30, 'calories': 250})
        activity_docs.append({'user_id': uid, 'name': 'Bike', 'duration_minutes': 45, 'calories': 400})
    db.activities.insert_many(activity_docs)

    # Teams
    team_doc = {'name': 'Alpha Team', 'member_ids': users[:2]}
    db.teams.insert_one(team_doc)

    # Workouts
    db.workouts.insert_one({'user_id': users[0], 'title': 'Morning Run', 'duration_minutes': 20})
    db.workouts.insert_one({'user_id': users[1], 'title': 'Evening Ride', 'duration_minutes': 45})

    # Leaderboard
    db.leaderboard.insert_one({'user_id': users[0], 'points': 150})
    db.leaderboard.insert_one({'user_id': users[1], 'points': 120})

    print('Populated octofit_db with test data (pymongo)')

    # Also create Django ORM objects so djongo sees the same data
    try:
        import sys
        import django
        # Ensure the Django project backend path is on sys.path when script is run directly
        backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        if backend_path not in sys.path:
            sys.path.insert(0, backend_path)
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
        django.setup()
        from octofit_app.models import UserProfile, Activity, Team, Workout, LeaderboardEntry

        # Create ORM entries if none exist
        if UserProfile.objects.count() == 0:
            orm_users = []
            for i in range(1, 6):
                u = UserProfile.objects.create(username=f'user{i}', email=f'user{i}@example.com')
                orm_users.append(u)

            for u in orm_users:
                Activity.objects.create(user=u, name='Run', duration_minutes=30, calories=250)
                Activity.objects.create(user=u, name='Bike', duration_minutes=45, calories=400)

            team = Team.objects.create(name='Alpha Team')
            team.members.set(orm_users[:2])

            Workout.objects.create(user=orm_users[0], title='Morning Run', duration_minutes=20)
            Workout.objects.create(user=orm_users[1], title='Evening Ride', duration_minutes=45)

            LeaderboardEntry.objects.create(user=orm_users[0], points=150)
            LeaderboardEntry.objects.create(user=orm_users[1], points=120)
    except Exception as e:
        print('Django ORM population failed:', repr(e))


if __name__ == '__main__':
    populate()
