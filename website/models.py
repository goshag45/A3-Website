from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.String(12), index=True, unique=True, nullable=False)
    address = db.Column(db.String(100), index=True, unique=True, nullable=False)
    comments = db.relationship('Comment', backref='user')

class Concert(db.Model):
    __tablename__ = 'concerts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    genre = db.Column(db.String(80))
    datetime = db.Column(db.DateTime, default=datetime.now())
    address = db.Column(db.String(80))
    city = db.Column(db.String(80))
    description = db.Column(db.String(400))
    tickets = db.Column(db.Integer)
    image = db.Column(db.String(400))
    comments = db.relationship('Comment', backref='concert')
    status = db.Column(db.String(20))
    def __repr__(self):
        return "<Name: {}>".format(self.name)

class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    user_name = db.Column(db.String(100), db.ForeignKey('users.name'))
    concert_id = db.Column(db.Integer, db.ForeignKey('concerts.id'))
    def __repr__(self):
        return "<Comment: {}>".format(self.text)

class Ticket(db.Model):
    __tablename__ ='tickets'
    name = db.Column(db.String(100), db.ForeignKey('users.name'))
    order_id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, index=True, nullable=False)
    genre = db.Column(db.String(80), db.ForeignKey('concerts.genre'))
    address = db.Column(db.String(100), db.ForeignKey('concerts.address'))
    individual_price = db.Column(db.Integer)
    total_price = db.Column(db.Integer)
    users = db.relationship('User', backref='ticket')