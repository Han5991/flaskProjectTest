from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class FcUser(db.Model):
    __tableName__ = 'fcUser'
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(64))
    userId = db.Column(db.String(8))
