from database.sprint_metrics_model import SprintMetrics
from config.database_config import db


def create_sprint_metrics(data):
    try:
        new_sprint_metrics = SprintMetrics(
            sprint_id=data["sprint_id"],
            team_size=data["team_size"],
            planned_story_points=data["planned_story_points"],
            blockers=data["blockers"],
            code_review_time=data["code_review_time"],
            bugs_found=data["bugs_found"],
            sentiment_score=data["sentiment_score"],
            sprint_duration=data["sprint_duration"],
            test_automation=data["test_automation"],
            domain_complexity=data["domain_complexity"],
            non_functional_requirements_complexity=data["non_functional_requirements_complexity"]
        )
        db.session.add(new_sprint_metrics)
        db.session.commit()
        return new_sprint_metrics.to_dict()
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}
    
def get_all_sprint_metrics():
    return [sprint_metrics.to_dict() for sprint_metrics in SprintMetrics.query.all()]

def get_sprint_metrics_by_id(sprint_metrics_id):
    sprint_metrics = SprintMetrics.query.get(sprint_metrics_id)
    return sprint_metrics.to_dict() if sprint_metrics else None

def update_sprint_metrics(sprint_metrics_id, data):
    sprint_metrics = SprintMetrics.query.get(sprint_metrics_id)
    if sprint_metrics:
        sprint_metrics.sprint_id = data.get("sprint_id", sprint_metrics.sprint_id)
        sprint_metrics.team_size = data.get("team_size", sprint_metrics.team_size)
        sprint_metrics.planned_story_points = data.get("planned_story_points", sprint_metrics.planned_story_points)
        sprint_metrics.blockers = data.get("blockers", sprint_metrics.blockers)
        sprint_metrics.code_review_time = data.get("code_review_time", sprint_metrics.code_review_time)
        sprint_metrics.bugs_found = data.get("bugs_found", sprint_metrics.bugs_found)
        sprint_metrics.sentiment_score = data.get("sentiment_score", sprint_metrics.sentiment_score)
        sprint_metrics.sprint_duration = data.get("sprint_duration", sprint_metrics.sprint_duration)
        sprint_metrics.test_automation = data.get("test_automation", sprint_metrics.test_automation)
        sprint_metrics.domain_complexity = data.get("domain_complexity", sprint_metrics.domain_complexity)
        sprint_metrics.non_functional_requirements_complexity = data.get("non_functional_requirements_complexity", sprint_metrics.non_functional_requirements_complexity)
        db.session.commit()
        return sprint_metrics.to_dict()
    return None

def delete_sprint_metrics(sprint_metrics_id):
    sprint_metrics = SprintMetrics.query.get(sprint_metrics_id)
    if sprint_metrics:
        db.session.delete(sprint_metrics)
        db.session.commit()
        return True
    return False
