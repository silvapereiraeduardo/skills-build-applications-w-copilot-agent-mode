from pymongo import MongoClient

def reset_db(uri='mongodb://localhost:27017', dbname='octofit_db'):
    client = MongoClient(uri)
    client.drop_database(dbname)
    print(f'Dropped database: {dbname}')

if __name__ == '__main__':
    reset_db()
