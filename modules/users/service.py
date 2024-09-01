from extensions import db
from models import User


def get_all_users():
    return db.session.execute(db.select(User)).scalars().all()
