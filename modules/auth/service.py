from extensions import db
from models import User
from sqlalchemy.exc import IntegrityError
from extensions import bcrypt
from flask_jwt_extended import create_access_token, create_refresh_token


class AuthService:
    @staticmethod
    def sign_in(username: str, password: str):
        user = db.session.query(User).filter_by(email=username).first()
        if user is None:
            return None, 400, "Incorrect username or password"

        if not bcrypt.check_password_hash(user.password, password):
            return None, 400, "Incorrect username or password"

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        user.refresh_token = refresh_token
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return None, 500, "Internal server error"

        return (
            {
                "user": user,
                "credentials": {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                },
            },
            None,
            None,
        )

    @staticmethod
    def refresh_token(user_id: int, refresh_token: str):
        user = db.session.query(User).get(user_id)
        if user is None:
            return None, 400, "User not found"

        if user.refresh_token != refresh_token:
            return None, 400, "Invalid refresh token"

        access_token = create_access_token(identity=user.id)
        refresh_token = create_refresh_token(identity=user.id)

        user.refresh_token = refresh_token
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()
            return None, 500, "Internal server error"

        return (
            {
                "access_token": access_token,
                "refresh_token": refresh_token,
            },
            None,
            None,
        )
