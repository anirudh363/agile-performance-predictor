from config.database_config import db



class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    name = db.Column(db.String(100), nullable=False)

    def __init__(self, name, user_id):
        self.user_id = user_id
        self.name = name

    def to_dict(self):
        return {"id": self.id, "user_id": self.user_id, "name": self.name}
