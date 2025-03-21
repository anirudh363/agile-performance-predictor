from database.teams_model import Team
from config.database_config import db


def check_if_team_exists(team_id):
    team = Team.query.get(team_id)
    return True if team else False

def create_team(data):
    try:
        new_team = Team(
            name=data["name"], 
            user_id=data["user_id"] if "user_id" in data else None
        )
        db.session.add(new_team)
        db.session.commit()
        return new_team.to_dict()
    except Exception as e:
        db.session.rollback()
        return {"error": str(e)}

def get_all_teams():
    return [team.to_dict() for team in Team.query.all()]

def get_team_by_id(team_id):
    team = Team.query.get(team_id)
    return team.to_dict() if team else None

def update_team(team_id, data):
    team = Team.query.get(team_id)
    if team:
        team.name = data.get("name", team.name)
        if "user_id" in data:
            team.user_id = data["user_id"]
        db.session.commit()
        return team.to_dict()
    return None

def delete_team(team_id):
    team = Team.query.get(team_id)
    if team:
        db.session.delete(team)
        db.session.commit()
        return True
    return False
