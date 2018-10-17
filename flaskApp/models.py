from flaskApp import db
from datetime import datetime

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(64), index=True, unique=True)
#     email = db.Column(db.String(120), index=True, unique=True)
#     password_hash = db.Column(db.String(128))
#     posts = db.relationship('Post', backref='author', lazy='dynamic')

#     def __repr__(self):
#         return '<User {}>'.format(self.username)    

# class Post(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     body = db.Column(db.String(140))
#     timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __repr__(self):
#         return '<Post {}>'.format(self.body)

class studentDemographics(db.Model):
    __tablename__ = 'student_demographics'
    id = db.Column(db.Integer, primary_key=True)
    # ncesid = db.Column(db.String(10), db.ForeignKey('user.id'))
    ncesid = db.Column(db.String(10))
    totalstudent = db.Column(db.Integer)
    stype = db.Column(db.String(20))
    value = db.Column(db.Integer)

    def __init__(self, ncesid, totalstudent, stype, value):
        self.ncesid = ncesid
        self.totalstudent = totalstudent
        self.stype = stype
        self.value = value


    def __repr__(self):
        return '<studentDemographics {}>'.format(self.ncesid)