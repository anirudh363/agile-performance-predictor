from flask import Flask
from database_config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_TRACK_MODIFICATIONS
from database_config import db
from routes.teams import teams_bp
from routes.sprints import sprints_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS

db.init_app(app)



# Register Blueprints
app.register_blueprint(teams_bp, url_prefix="/api/teams")
app.register_blueprint(sprints_bp, url_prefix="/api/sprints")



@app.route('/')
def home():
    return "Welcome to the Agile Performance Prediction API"


# Create tables
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)

