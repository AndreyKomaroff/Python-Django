from flask_sqlalchemy import SQLAlchemy
from flask_user import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
   __tablename__ = 'users'
   id = db.Column(db.Integer, primary_key=True)
   email = db.Column(db.String(255), nullable=False, unique=True)
   password = db.Column(db.String(255), nullable=False, server_default='')
   active = db.Column(db.Boolean(), nullable=False, server_default='0')

db.create_all()