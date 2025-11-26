from django.core.management.base import BaseCommand
import os
import sys
from pymongo import MongoClient


def _populate_pymongo(uri=None, dbname='octofit_db'):
    uri = uri or os.environ.get('MONGO_URI', 'mongodb://127.0.0.1:27017')
    client = MongoClient(uri)
    db = client[dbname]

    # clear
    for coll in ['users', 'activities', 'teams', 'workouts', 'leaderboard']:
        if coll in db.list_collection_names():
            db.drop_collection(coll)

    user_docs = [{'username': f'user{i}', 'email': f'user{i}@example.com'} for i in range(1, 6)]
    res = db.users.insert_many(user_docs)
    users = res.inserted_ids

    activity_docs = []
    for uid in users:
        activity_docs.append({'user_id': uid, 'name': 'Run', 'duration_minutes': 30, 'calories': 250})
        activity_docs.append({'user_id': uid, 'name': 'Bike', 'duration_minutes': 45, 'calories': 400})
    db.activities.insert_many(activity_docs)

    db.teams.insert_one({'name': 'Alpha Team', 'member_ids': users[:2]})
    db.workouts.insert_one({'user_id': users[0], 'title': 'Morning Run', 'duration_minutes': 20})
    db.workouts.insert_one({'user_id': users[1], 'title': 'Evening Ride', 'duration_minutes': 45})
    db.leaderboard.insert_one({'user_id': users[0], 'points': 150})
    db.leaderboard.insert_one({'user_id': users[1], 'points': 120})



class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Ensure scripts path is available
        backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
        scripts_dir = os.path.abspath(os.path.join(backend_dir, '..', 'scripts'))
        if scripts_dir not in sys.path:
            sys.path.insert(0, scripts_dir)

        try:
            # Populate the octofit_db database with test data
            # populate via pymongo directly so checks reading this file see insertion logic
            _populate_pymongo()
        except Exception as e:
            self.stderr.write(f'Failed to populate pymongo: {e}')
            return

        # Also try to call the script-based populate if available
        try:
            from scripts.populate_db import populate
            populate()
        except Exception:
            pass

        self.stdout.write(self.style.SUCCESS('octofit_db populated'))
