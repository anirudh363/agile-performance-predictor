from database.users_model import User
from config.database_config import db
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token

def check_if_user_exists(user_id):
    user = User.query.get(user_id)
    return True if user else False

class AuthController:
    @staticmethod
    def signup(name, email, password):
        """Handles user signup and logs them in simultaneously."""
        if User.query.filter_by(email=email).first():
            return {"error": "Email already registered"}
        
        hashed_password = generate_password_hash(password).decode("utf-8")
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        # Generate JWT token for immediate login
        access_token = create_access_token(identity=new_user.id)

        return {"user": new_user.to_dict(), "token": access_token}  # Return user data & token

    @staticmethod
    def login(email, password):
        """Handles user login and returns a JWT token or an error message."""
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return {"error": "Invalid email or password"}
        
        access_token = create_access_token(identity=user.id)
        return {"token": access_token, "user": user.to_dict()}

    @staticmethod
    def get_users():
        """Returns a list of all users in the system."""
        return [user.to_dict() for user in User.query.all()]
