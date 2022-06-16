from typing import AsyncGenerator, Generator
from sqlmodel import Session, create_engine

from sqlmodel.ext.asyncio.session import AsyncSession
from sqlalchemy.ext.asyncio import create_async_engine
from app.core.config import settings


sync_engine = create_engine(
    settings.API_DATABASE_SYNC_URI, echo=False, future=True, pool_pre_ping=True
)


def get_sync_session() -> Generator[Session, None, None]:
    with Session(sync_engine) as session:
        yield session


async_engine = create_async_engine(
    settings.API_DATABASE_ASYNC_URI, echo=False, future=True, pool_pre_ping=True
)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with AsyncSession(async_engine) as session:
        yield session
