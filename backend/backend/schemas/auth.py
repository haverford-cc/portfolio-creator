from pydantic import BaseModel, EmailStr, validator

from backend.constants import PASSWORD_MIN_LENGTH


class NewUser(BaseModel):
    """Represents a new user."""
    email: EmailStr

    password1: str
    password2: str

    name: str

    @validator("password1")
    def password_length(cls, p1: str) -> str:
        """Ensure password is at least 8 characters long."""
        if len(p1) < PASSWORD_MIN_LENGTH:
            raise ValueError("Password is too short")

        return p1

    @validator("password2")
    def passwords_match(cls, p2: str, values: dict[str, str]):
        """Ensure both passwords match."""
        if "password1" in values and values["password1"] != p2:
            raise ValueError("Passwords do not match")

        return p2


class User(BaseModel):
    """Represents a user."""
    email: EmailStr
    password: str
