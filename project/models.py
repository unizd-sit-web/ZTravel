from project import bcrypt
from project import db

user_favorites = db.Table('user_favorites',
                          db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
                          db.Column('location_id', db.Integer, db.ForeignKey('locations.id')))


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.VARCHAR(length=100), unique=True, nullable=False)
    password_hash = db.Column(db.VARCHAR(length=60), nullable=False)
    newsletter = db.Column(db.Boolean, nullable=False)
    favorites = db.relationship('Location', secondary=user_favorites, backref='users')

    def __repr__(self):
        return f"Email: {self.email}    ID: {self.id}"

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')


class Location(db.Model):
    __tablename__ = 'locations'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(length=60), nullable=False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Location: {self.name}"
