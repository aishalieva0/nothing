from app import db
from werkzeug.security import generate_password_hash


class AdminUser(db.Model):
    __tablename__ = "admins"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    @classmethod
    def create(cls, username, email, password):
        existing_admin_user = cls.query.filter_by(username=username).first()
        if existing_admin_user:
            raise ValueError("Username already exists")

        password = generate_password_hash(password)

        new_admin_user = cls(username=username, email=email, password=password)

        db.session.add(new_admin_user)
        db.session.commit()

        return new_admin_user
