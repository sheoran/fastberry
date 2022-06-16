import logging
from sqlalchemy.orm import Session
from app.core.config import settings
from app.core.security import get_password_hash
from app.core.db import get_sync_session
from app.models import UserModel

log = logging.getLogger(__name__)

# make sure all SQL Alchemy models are imported (app.db.base) before initializing DB
# otherwise, SQL Alchemy might fail to initialize relationships properly
# for more details: https://github.com/tiangolo/full-stack-fastapi-postgresql/issues/28


def init_db(db: Session = None) -> None:
    db = next(get_sync_session()) if db is None else db
    user = (
        db.query(UserModel)
        .filter(UserModel.email == settings.API_SERVICE_DEFAULT_SUPERUSER_NAME)
        .first()
    )
    if not user:
        user = UserModel(
            email=settings.API_SERVICE_DEFAULT_SUPERUSER_NAME,
            password=get_password_hash(settings.API_SERVICE_DEFAULT_SUPERUSER_PASSWORD),
            full_name="Default Super User",
            is_superuser=True,
        )
        db.add(user)
        db.commit()


def main() -> None:
    log.info("Creating initial data")
    init_db()
    log.info("Initial data created")


if __name__ == "__main__":
    main()
