from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import app.models

app = Flask(__name__)
app.config.from_pyfile("config.py")

db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.routes.admin_routes import admin_bp
from app.routes.company_routes import company_bp
from app.routes.problem_routes import problem_bp
from app.routes.user_routes import user_bp

app.register_blueprint(admin_bp)
app.register_blueprint(company_bp)
app.register_blueprint(problem_bp)
app.register_blueprint(user_bp)
