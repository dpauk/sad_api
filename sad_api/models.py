from datetime import datetime

from . import db


class Customer(db.Model):
    __tablename__ = 'customers'


class Account(db.Model):
    __tablename__ = 'accounts'


class Transactions(db.Model):
    __tablename__ = 'transactions'


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, nullable=False)
    password = db.Column(db.String(8), nullable=False)
    accounts = db.relationship('Account', backref='users', lazy='dynamic')
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    dormant = db.Column(db.String(1), default='N')
