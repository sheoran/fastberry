from sqlmodel import SQLModel, Field
from typing import Optional
from pydantic import EmailStr
from sqlalchemy import Column, String
from .base import ModelBase


class UserBaseModel(SQLModel):
    email: EmailStr = Field(sa_column=Column("email", String, unique=True, index=True))
    full_name: Optional[str] = None
    is_active: bool = True
    is_superuser: bool = False


class UserModel(ModelBase, UserBaseModel, table=True):
    password: str


class UserReadModel(ModelBase, UserBaseModel):
    pass


class UserCreateModel(UserBaseModel):
    password: str
