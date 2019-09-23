"""Example of SQLAlchemy One-to-One."""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()


class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50))

    employee = db.relationship("Employee",
                               uselist=False)
    # !end User

    def __repr__(self):
        return "<User email={}>".format(self.email)


class Employee(db.Model):

    __tablename__ = 'employees'

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        primary_key=True)
    salary = db.Column(db.Integer)

    user = db.relationship("User",
                           uselist=False)
    # !end Employee

    def __repr__(self):
        return "<Employee id={}>".format(self.user_id)


def connect_to_db(app):
    """Connect to database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///one-to-one"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == '__main__':
    import os

    os.system("dropdb one-to-one")
    os.system("createdb one-to-one")

    connect_to_db(app)

    # Make our tables
    db.create_all()

    # Add users
    joel = User(user_id=1, email="joel@hackbrightacademy.com")
    meggie = User(user_id=2, email="meggie@hackbrightacademy.com")
    rachel = User(user_id=3, email="rachel@hackbrightacademy.com")

    #Add Empolyees
    j_burton = Employee(user_id=1, salary=90000)


    # add users and empolyees to session
    db.session.add(joel)
    db.session.add(meggie)
    db.session.add(rachel)
    db.session.add(j_burton)
    db.session.commit()

    # Test that this worked
    employee_1 = Employee.query.filter_by(user_id=1).one()
    employee_1.data.email = 'joel@hackbrightacademy.com'
