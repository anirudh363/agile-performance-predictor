from database_config import db

class Sprints(db.Model):
    __tablename__ = 'sprints'

    id = db.Column(db.Integer, primary_key=True)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id', ondelete="CASCADE"), nullable=False)
    sprint_index = db.Column(db.Integer, nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    planned_story_points = db.Column(db.Integer, nullable=False)

    def __init__(self, team_id, sprint_index, start_date, end_date, planned_story_points):
        self.team_id = team_id
        self.sprint_index = sprint_index
        self.start_date = start_date
        self.end_date = end_date
        self.planned_story_points = planned_story_points

    def to_dict(self):
        return {
            "id": self.id,
            "team_id": self.team_id,
            "sprint_index": self.sprint_index,
            "start_date": self.start_date.strftime("%Y-%m-%d %H:%M:%S"), 
            "end_date": self.end_date.strftime("%Y-%m-%d %H:%M:%S"),      
            "planned_story_points": self.planned_story_points
        }
