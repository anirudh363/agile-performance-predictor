from database.sprint_predictions_model import SprintPredictions
from config.database_config import db

def create_sprint_prediction(data):
    try:
        new_sprint_prediction = SprintPredictions(
            sprint_id=data["sprint_id"],
            user_id=data["user_id"],
            predicted_story_points=data["predicted_story_points"],
            actual_completed_story_points=data["actual_completed_story_points"] if "actual_completed_story_points" in data else None
        )
        db.session.add(new_sprint_prediction)
        db.session.commit()
        return new_sprint_prediction.to_dict()
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}
    
def get_all_sprint_predictions():
    return [sprint_prediction.to_dict() for sprint_prediction in SprintPredictions.query.all()]

def get_sprint_prediction_by_id(sprint_prediction_id):
    sprint_prediction = SprintPredictions.query.get(sprint_prediction_id)
    return sprint_prediction.to_dict() if sprint_prediction else None

def update_sprint_prediction(sprint_prediction_id, data):
    sprint_prediction = SprintPredictions.query.get(sprint_prediction_id)
    if sprint_prediction:
        sprint_prediction.sprint_id = data.get("sprint_id", sprint_prediction.sprint_id)
        sprint_prediction.user_id = data.get("user_id", sprint_prediction.user_id)
        sprint_prediction.predicted_story_points = data.get("predicted_story_points", sprint_prediction.predicted_story_points)
        if "actual_completed_story_points" in data:
            sprint_prediction.actual_completed_story_points = data["actual_completed_story_points"]
        db.session.commit()
        return sprint_prediction.to_dict()
    return None

def delete_sprint_prediction(sprint_prediction_id):
    sprint_prediction = SprintPredictions.query.get(sprint_prediction_id)
    if sprint_prediction:
        db.session.delete(sprint_prediction)
        db.session.commit()
        return True
    return False
