from app import db


class Problem(db.Model):
    __tablename__ = "problems"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    company_id = db.Column(db.Integer, nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default="Pending")  # Pending, Resolved

    @staticmethod
    def create(user_id, company_id, description):
        new_problem = Problem(
            user_id=user_id, company_id=company_id, description=description
        )
        db.session.add(new_problem)
        db.session.commit()
        return new_problem

    @staticmethod
    def get_all():
        return Problem.query.all()
