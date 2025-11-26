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

    # Insert users
    users = []
    for i in range(1, 6):
        doc = {'username': f'user{i}', 'email': f'user{i}@example.com'}
        users.append(db.users.insert_one(doc).inserted_id)

    # Insert activities (2 per user)
    for uid in users:
        db.activities.insert_one({'user_id': uid, 'name': 'Run', 'duration_minutes': 30, 'calories': 250})
        db.activities.insert_one({'user_id': uid, 'name': 'Bike', 'duration_minutes': 45, 'calories': 400})

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


if __name__ == '__main__':
    populate()
