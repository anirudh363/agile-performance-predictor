from database_config import db

class SprintMetrics(db.Model):
    __tablename__ = 'sprint_metrics'

    id = db.Column(db.Integer, primary_key=True)
    sprint_id = db.Column(db.Integer, db.ForeignKey('sprints.id', ondelete="CASCADE"), nullable=False)
    team_size = db.Column(db.Integer, nullable=False)
    planned_story_points = db.Column(db.Integer, nullable=False)
    blockers = db.Column(db.Integer, nullable=False)
    code_review_time = db.Column(db.Numeric(10, 2), nullable=False)
    bugs_found = db.Column(db.Integer, nullable=False)
    sentiment_score = db.Column(db.Integer, nullable=False)  
    sprint_duration = db.Column(db.Integer, nullable=False)
    test_automation = db.Column(db.Boolean, nullable=False)
    domain_complexity = db.Column(db.Integer, nullable=False)
    non_functional_requirements_complexity = db.Column(db.Integer, nullable=False)

    def __init__(self, sprint_id, team_size, planned_story_points, blockers, code_review_time, bugs_found, sentiment_score, sprint_duration, test_automation, domain_complexity, non_functional_requirements_complexity):
        self.sprint_id = sprint_id
        self.team_size = team_size
        self.planned_story_points = planned_story_points
        self.blockers = blockers
        self.code_review_time = code_review_time
        self.bugs_found = bugs_found
        self.sentiment_score = sentiment_score
        self.sprint_duration = sprint_duration
        self.test_automation = test_automation
        self.domain_complexity = domain_complexity
        self.non_functional_requirements_complexity = non_functional_requirements_complexity

    def to_dict(self):
        return {
            "id": self.id,
            "sprint_id": self.sprint_id,
            "team_size": self.team_size,
            "planned_story_points": self.planned_story_points,
            "blockers": self.blockers,
            "code_review_time": float(self.code_review_time), 
            "bugs_found": self.bugs_found,
            "sentiment_score": self.sentiment_score,
            "sprint_duration": self.sprint_duration,
            "test_automation": self.test_automation,
            "domain_complexity": self.domain_complexity,
            "non_functional_requirements_complexity": self.non_functional_requirements_complexity,
        }
