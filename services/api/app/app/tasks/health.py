from app.core import celery_app


@celery_app.task
def echo_msg(word: str) -> str:
    return f"Echo: {word}"
