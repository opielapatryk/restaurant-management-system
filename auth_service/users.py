# Third party modules
from sqlalchemy import (
    LargeBinary, 
    Column, 
    String, 
    Integer,
    Boolean, 
    UniqueConstraint, 
    PrimaryKeyConstraint
)
from sqlalchemy.orm import declarative_base

# Create database declarative base
Base = declarative_base()

class User(Base):
    """Models a user table"""
    __tablename__ = "users"
    email = Column(String(225), nullable=False, unique=True)
    id = Column(Integer, nullable=False, primary_key=True)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String(225), nullable=False)
    is_active = Column(Boolean, default=False)

    UniqueConstraint("email", name="uq_user_email")
    PrimaryKeyConstraint("id", name="pk_user_id")

    def __repr__(self):
        """Returns string representation of model instance"""
        return "<User {full_name!r}>".format(full_name=self.full_name)