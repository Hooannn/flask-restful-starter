from extensions import db
from models import User
from sqlalchemy.exc import IntegrityError
from extensions import bcrypt


class UserService:
    @staticmethod
    def get_all_users():
        return db.session.execute(db.select(User)).scalars().all()

    @staticmethod
    def create_user(email: str, password: str):
        existing_user = db.session.query(User).filter_by(email=email).first()
        if existing_user is not None:
            return None, 409, "User already exists"

        try:
            user = User(
                email=email,
                password=bcrypt.generate_password_hash(password).decode("utf-8"),
            )
            db.session.add(user)
            db.session.commit()
            return user, None, None
        except IntegrityError as e:
            db.session.rollback()
            return None, 409, str(e)

    @staticmethod
    def get_user_by_id(user_id: int):
        user = User.query.get(user_id)
        if not user:
            return None, 404, "User not found"
        return user, None, None
