from sqlalchemy import Integer, String

from backend.models import Base


class User(Base):
    """Represents a user."""

    __tablename__ = "users"

    id = Integer(primary_key=True)
    email = String(length=255, unique=True, nullable=False)
    password_hash = String(nullable=False)
