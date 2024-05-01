from app import db

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(50), default="Pending")  # Pending, Approved, Rejected

    @staticmethod
    def create(name, email):
        new_company = Company(name=name, email=email)
        db.session.add(new_company)
        db.session.commit()
        return new_company

    @staticmethod
    def get_all():
        return Company.query.all()