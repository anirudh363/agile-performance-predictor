from database.sprints_model import Sprints
from config.database_config import db


def check_if_sprint_exists(sprint_id):
    sprint = Sprints.query.get(sprint_id)
    return True if sprint else False

def create_sprint(data):
    try:
        new_sprint = Sprints(
            team_id=data["team_id"], 
            sprint_index=data["sprint_index"], 
            start_date=data["start_date"], 
            end_date=data["end_date"], 
            planned_story_points=data["planned_story_points"]
            )
        db.session.add(new_sprint)
        db.session.commit()
        return new_sprint.to_dict()
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}
    
def get_all_sprints(): 
    return [sprint.to_dict() for sprint in Sprints.query.all()]

def get_sprint_by_id(sprint_id):
    sprint = Sprints.query.get(sprint_id)
    return sprint.to_dict() if sprint else None

def update_sprint(sprint_id, data):
    sprint = Sprints.query.get(sprint_id)
    if sprint:
        sprint.team_id = data.get("team_id", sprint.team_id)
        sprint.sprint_index = data.get("sprint_index", sprint.sprint_index)
        sprint.start_date = data.get("start_date", sprint.start_date)
        sprint.end_date = data.get("end_date", sprint.end_date)
        sprint.planned_story_points = data.get("planned_story_points", sprint.planned_story_points)
        db.session.commit()
        return sprint.to_dict()
    return None

def delete_sprint(sprint_id):
    sprint = Sprints.query.get(sprint_id)
    if sprint:
        db.session.delete(sprint)
        db.session.commit()
        return True
    return False