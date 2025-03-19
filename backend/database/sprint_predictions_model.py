from config.database_config import db

class SprintPredictions(db.Model):
    __tablename__ = 'sprint_predictions'

    id = db.Column(db.Integer, primary_key=True)
    sprint_id = db.Column(db.Integer, db.ForeignKey('sprints.id', ondelete="CASCADE"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete="CASCADE"), nullable=True)
    predicted_story_points = db.Column(db.Integer, nullable=False)
    actual_completed_story_points = db.Column(db.Integer, nullable=True)

    def __init__(self, sprint_id, user_id, predicted_story_points, actual_completed_story_points):
        self.sprint_id = sprint_id
        self.user_id = user_id
        self.predicted_story_points = predicted_story_points
        self.actual_completed_story_points = actual_completed_story_points

    def to_dict(self):
        return {
            "id": self.id,
            "sprint_id": self.sprint_id,
            "user_id": self.user_id,
            "predicted_story_points": self.predicted_story_points,
            "actual_completed_story_points": self.actual_completed_story_points
        }
    