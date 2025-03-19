from database.training_data_model import TrainingData
from config.database_config import db


def create_training_data(data):
    try: 
        new_training_data = TrainingData(
            team_size=data["team_size"],
            planned_story_points=data["planned_story_points"],
            completed_story_points=data["completed_story_points"],
            blockers=data["blockers"],
            code_review_time=data["code_review_time"],
            bugs_found=data["bugs_found"],
            sentiment_score=data["sentiment_score"],
            sprint_duration=data["sprint_duration"],
            test_automation=data["test_automation"],
            domain_complexity=data["domain_complexity"],
            non_functional_requirements_complexity=data["non_functional_requirements_complexity"],
            sprint_start_date=data["sprint_start_date"],
            sprint_end_date=data["sprint_end_date"]
        )
        db.session.add(new_training_data)
        db.session.commit()
        return new_training_data.to_dict()
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}
    
def get_all_training_data():
    return [training_data.to_dict() for training_data in TrainingData.query.all()]

def get_training_data_by_id(training_data_id):
    training_data = TrainingData.query.get(training_data_id)
    return training_data.to_dict() if training_data else None

def update_training_data(training_data_id, data):
    training_data = TrainingData.query.get(training_data_id)
    if training_data:
        training_data.team_size = data.get("team_size", training_data.team_size)
        training_data.planned_story_points = data.get("planned_story_points", training_data.planned_story_points)
        training_data.completed_story_points = data.get("completed_story_points", training_data.completed_story_points)
        training_data.blockers = data.get("blockers", training_data.blockers)
        training_data.code_review_time = data.get("code_review_time", training_data.code_review_time)
        training_data.bugs_found = data.get("bugs_found", training_data.bugs_found)
        training_data.sentiment_score = data.get("sentiment_score", training_data.sentiment_score)
        training_data.sprint_duration = data.get("sprint_duration", training_data.sprint_duration)
        training_data.test_automation = data.get("test_automation", training_data.test_automation)
        training_data.domain_complexity = data.get("domain_complexity", training_data.domain_complexity)
        training_data.non_functional_requirements_complexity = data.get("non_functional_requirements_complexity", training_data.non_functional_requirements_complexity)
        training_data.sprint_start_date = data.get("sprint_start_date", training_data.sprint_start_date)
        training_data.sprint_end_date = data.get("sprint_end_date", training_data.sprint_end_date)
        db.session.commit()
        return training_data.to_dict()
    return None

def delete_training_data(training_data_id):
    training_data = TrainingData.query.get(training_data_id)
    if training_data:
        db.session.delete(training_data)
        db.session.commit()
        return training_data.to_dict()
    return None
