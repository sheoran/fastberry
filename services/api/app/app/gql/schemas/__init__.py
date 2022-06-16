import strawberry
from .user import UserQuery, UserMutation
from .tasks import TaskMutation


@strawberry.type
class Query(UserQuery):
    pass


@strawberry.type
class Mutation(UserMutation, TaskMutation):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)
