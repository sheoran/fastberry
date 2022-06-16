from datetime import datetime
import uuid
from typing import Optional
from sqlalchemy import Column, DateTime
from sqlmodel import SQLModel, Field


class ModelBase(SQLModel):
    """
    Base class for database models.
    """

    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    created_at: Optional[datetime] = Field(
        sa_column=Column(DateTime(timezone=True), default=datetime.utcnow)
    )
    updated_at: Optional[datetime] = Field(
        sa_column=Column(
            DateTime(timezone=True), onupdate=datetime.utcnow, default=datetime.utcnow
        )
    )
