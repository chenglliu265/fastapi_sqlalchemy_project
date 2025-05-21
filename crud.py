from sqlalchemy import select
from sqlalchemy.orm import Session
from models import User
from schemas import UserCreate, UserUpdate


def get_user(db: Session, user_id: int):
    return db.execute(select(User).filter(User.id == user_id)).scalars().first()


def create_user(db: Session, user: UserCreate):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user_by_email(db: Session, email: str):
    result = db.execute(select(User).filter(User.email == email))
    return result.scalars().first()


def update_user(db: Session, user_id: int, user_update: UserUpdate):
    db_user = get_user(db, user_id)
    if not db_user:
        return None
    update_data = user_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user
