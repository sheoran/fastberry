import strawberry
from app import tasks
from strawberry.scalars import JSON


@strawberry.type
class TaskMutation:
    @strawberry.mutation
    async def ping_celery(self, info, word: str) -> JSON:
        result = tasks.echo_msg.delay(word).get()
        return {"response": result}
