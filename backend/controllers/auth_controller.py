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

        return {"user": new_user.to_dict(), "token": access_token}  

    @staticmethod
    def login(email, password):
        """Handles user login and returns a JWT token or an error message."""
        user = User.query.filter_by(email=email).first()
        if not user or not check_password_hash(user.password, password):
            return {"error": "Invalid email or password"}
        
        access_token = create_access_token(identity=user.id)
        return {"token": access_token, "user": user.to_dict()}
    
    @staticmethod
    def change_password(email, old_password, new_password):
        """Changes a user's password."""
        user = User.query.filter_by(email=email).first()
        if not user:
            return {"error": "User not found"}
        if not check_password_hash(user.password, old_password):
            return {"error": "Invalid password"}
        
        # Hash the new password and update
        user.password = generate_password_hash(new_password).decode("utf-8")
        db.session.commit()

        # Generate JWT token for immediate login
        access_token = create_access_token(identity=user.id)

        return {"user": user.to_dict(), "token": access_token}

    @staticmethod
    def get_users():
        """Returns a list of all users in the system."""
        return [user.to_dict() for user in User.query.all()]
    
    @staticmethod
    def get_user_by_id(user_id):
        """Returns a user by their ID."""
        user = User.query.get(user_id)
        return user.to_dict() if user else None
    
    @staticmethod
    def update_user(user_id, data):
        """Updates a user's details."""
        user = User.query.get(user_id)
        if user:
            user.name = data.get("name", user.name)
            user.email = data.get("email", user.email)
            if "password" in data:
                user.password = generate_password_hash(data["password"]).decode("utf-8")
            db.session.commit()
            return user.to_dict()
        return None
    
    @staticmethod
    def delete_user(user_id):
        """Deletes a user by their ID."""
        user = User.query.get(user_id)
        if user:
            db.session.delete(user)
            db.session.commit()
            return True
        return False
