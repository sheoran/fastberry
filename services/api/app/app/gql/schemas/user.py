import strawberry
from sqlmodel import select
from typing import List
from app.models import UserReadModel, UserModel, UserCreateModel


# ####
# Note:
# We are using an experimental feature. It Saves us time today and in future
# If the api changes we can always customize the Stawberry type and remain
# backward comptible.
@strawberry.experimental.pydantic.type(UserReadModel, all_fields=True)
class UserType:
    pass


@strawberry.experimental.pydantic.input(UserCreateModel, all_fields=True)
class UserInput:
    pass


@strawberry.type
class UserQuery:
    @strawberry.field
    async def all_users(self, info) -> List[UserType]:
        db = info.context.db
        result = await db.exec(select(UserModel))
        return [UserReadModel.from_orm(i) for i in result.all()]


@strawberry.type
class UserMutation:
    @strawberry.mutation
    async def create_user(self, info, user: UserInput) -> UserType:
        db = info.context.db
        obj = UserModel.from_orm(user)
        db.add(obj)
        await db.commit()
        await db.refresh(obj)
        return UserReadModel.from_orm(obj)
