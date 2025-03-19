from flask import Flask 
from flask_jwt_extended import JWTManager

from config.database_config import SQLALCHEMY_DATABASE_URI_LOCAL, SQLALCHEMY_DATABASE_URI_TEMBO, SQLALCHEMY_TRACK_MODIFICATIONS
from config.database_config import db
from config.auth_config import JWT_SECRET_KEY

from routes.teams import teams_bp
from routes.sprints import sprints_bp
from routes.sprint_metrics import sprint_metrics_bp
from routes.training_data import training_data_bp
from routes.auth import auth_bp
from routes.sprint_predictions import sprint_predictions_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI_TEMBO
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = SQLALCHEMY_TRACK_MODIFICATIONS
app.config["JWT_SECRET_KEY"] = JWT_SECRET_KEY

db.init_app(app)
jwt = JWTManager(app)


# Register Blueprints
app.register_blueprint(teams_bp, url_prefix="/api/teams")
app.register_blueprint(sprints_bp, url_prefix="/api/sprints")
app.register_blueprint(sprint_metrics_bp, url_prefix="/api/sprint-metrics")
app.register_blueprint(training_data_bp, url_prefix="/api/training-data")
app.register_blueprint(auth_bp, url_prefix="/api/auth")
app.register_blueprint(sprint_predictions_bp, url_prefix="/api/sprint-predictions")


@app.route('/')
def home():
    return "Welcome to the Agile Performance Prediction API"


# Create tables
with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)

