from app import db
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy(app)

class AdminUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

    @staticmethod
    def create(username, email):
        new_admin_user = AdminUser(username=username, email=email)
        db.session.add(new_admin_user)
        db.session.commit()
        return new_admin_user

    @staticmethod
    def get_all():
        return AdminUser.query.all()
