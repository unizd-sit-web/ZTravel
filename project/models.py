from project import bcrypt
from project import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.VARCHAR(length=100), unique=True, nullable=False)
    password_hash = db.Column(db.VARCHAR(length=60), nullable=False)


    def __repr__(self):
        return f"Email: {self.email}    ID: {self.id}"

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')


