from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,DeclarativeBase

SQLALCHEMY_DATABASE_URL = 'mysql+mysqlconnector://root:root@localhost/users'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def init_db():
    Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

