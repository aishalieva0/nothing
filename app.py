from flask import Flask


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"


db.init_app(app)
with app.app_context():
    db.create_all()

from routes import *


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, threaded=True)
