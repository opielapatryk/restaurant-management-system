# Third party modules
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Local modules
from users import User, Base
from auth_utils import get_password_hash

# built-in modules
import os

# Create database engine
engine = create_engine(f"postgresql://postgres:postgres@{os.getenv('PG_HOST','localhost')}/auth", echo=True, future=True)

# Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Database session generator"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)

    db = SessionLocal()

    # Check if the initial user exists
    user = db.query(User).filter(User.email == "email").first()
    if not user:
        # Insert the initial user
        initial_user = User(
            id=1,
            email="email",
            hashed_password=get_password_hash("password"),
            full_name="Joe Doe",
            is_active=True
        )
        db.add(initial_user)
        db.commit()
        db.refresh(initial_user)
        print("Initial user created.")
    else:
        print("Initial user already exists.")
    
    db.close()