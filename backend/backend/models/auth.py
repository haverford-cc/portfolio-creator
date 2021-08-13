from sqlalchemy import Column, Integer, String

from backend.models import Base


class User(Base):
    """Represents a user."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(length=255), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
