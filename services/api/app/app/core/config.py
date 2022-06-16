import secrets
from typing import Any, Dict, List, Optional, Union
from pydantic import (
    AnyHttpUrl,
    BaseSettings,
    EmailStr,
    PostgresDsn,
    validator,
    RedisDsn,
    AmqpDsn,
)


class Settings(BaseSettings):
    # ###########################################################################
    # General Settings
    DEPLOYMENT_NAME: str = "dev"
    GQL_STR: str = "/graphql"

    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # ###########################################################################
    # API_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    API_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("API_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    # ###########################################################################
    # Database
    API_SERVICE_DB_HOST: str
    API_SERVICE_DB_PORT: int
    API_SERVICE_DB_USER: str
    API_SERVICE_DB_PASSWORD: str
    API_SERVICE_DB_NAME: str
    API_DATABASE_ASYNC_URI: Optional[PostgresDsn] = None
    API_DATABASE_SYNC_URI: Optional[PostgresDsn] = None

    @validator("API_DATABASE_ASYNC_URI", pre=True)
    def assemble_db_async_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql+asyncpg",
            user=values.get("API_SERVICE_DB_USER"),
            password=values.get("API_SERVICE_DB_PASSWORD"),
            host=values.get("API_SERVICE_DB_HOST"),
            port=str(values.get("API_SERVICE_DB_PORT")),
            path=f"/{values.get('API_SERVICE_DB_NAME') or ''}",
        )

    @validator("API_DATABASE_SYNC_URI", pre=True)
    def assemble_db_sync_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("API_SERVICE_DB_USER"),
            password=values.get("API_SERVICE_DB_PASSWORD"),
            host=values.get("API_SERVICE_DB_HOST"),
            port=str(values.get("API_SERVICE_DB_PORT")),
            path=f"/{values.get('API_SERVICE_DB_NAME') or ''}",
        )

    # ###########################################################################
    # CELERY SETTINGS
    API_CELERY_ACCEPT_CONTENT: List[str] = ["json"]
    API_CELERY_BROKER_URL: AmqpDsn
    API_CELERY_ENABLE_REMOTE_CONTROL: bool = True
    API_CELERY_ENABLE_REMOTE_CONTROL: bool = True
    API_CELERY_RESULT_API: RedisDsn
    API_CELERY_RESULT_CACHE_MAX: int = -1
    API_CELERY_RESULT_SERIALIZER: str = "json"
    API_CELERY_SEND_TASK_EVENTS = True
    API_CELERY_TASK_ACKS_LATE: bool = True
    API_CELERY_TASK_ALWAYS_EAGER: bool = False
    API_CELERY_TASK_ANNOTATIONS: Dict[str, Any] = {
        "celery.chord_unlock": {"task_soft_time_limit": 300, "default_retry_delay": 5}
    }
    API_CELERY_TASK_REJECT_ON_WORKER_LOST: bool = True
    API_CELERY_TASK_RESULT_EXPIRES: int = 7200  # time in seconds
    API_CELERY_TASK_SEND_SENT_EVENT: bool = True
    API_CELERY_TASK_SERIALIZER: str = "json"
    API_CELERY_TASK_TIME_LIMIT = 24 * 3600  # A task can run for max of 24hrs
    API_CELERY_TASK_TRACK_STARTED: bool = True
    API_CELERY_TIMEZONE: str = "UTC"
    API_CELERY_WORKER_HIJACK_ROOT_LOGGER: bool = False
    API_CELERY_WORKER_LOST_WAIT = 59
    API_CELERY_WORKER_MAX_TASKS_PER_CHILD = 20
    API_CELERY_WORKER_POOL_RESTARTS: bool = True
    API_CELERY_WORKER_PREFETCH_MULTIPLIER: int = 1

    # ###########################################################################
    # Beats schedule
    API_CELERY_BEAT_SCHEDULE: dict = {}

    # ###########################################################################
    # SuperUser
    API_SERVICE_DEFAULT_SUPERUSER_NAME: EmailStr
    API_SERVICE_DEFAULT_SUPERUSER_PASSWORD: str

    class Config:
        case_sensitive = True


settings = Settings()
