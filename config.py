from sqlalchemy import create_engine

db = {
    'user': 'root',
    'password': 'dnl1vhr2',
    'host': 'brandi.c5my9kjknh3g.us-east-2.rds.amazonaws.com',
    'port': 3306,
    'database': 'brandi'
}

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
