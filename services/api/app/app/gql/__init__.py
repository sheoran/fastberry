from fastapi import Depends
from strawberry.fastapi import BaseContext
from sqlmodel.ext.asyncio.session import AsyncSession
from strawberry.fastapi import GraphQLRouter
from app.core.db import get_async_session
from strawberry.subscriptions import GRAPHQL_WS_PROTOCOL
from app.gql.schemas import schema


class CustomContext(BaseContext):
    def __init__(self, db: AsyncSession):
        self.db = db


def custom_context_dependency(
    db: AsyncSession = Depends(get_async_session),
) -> CustomContext:
    return CustomContext(db=db)


async def get_context(
    custom_context=Depends(custom_context_dependency),
):
    return custom_context


def get_gql_router() -> GraphQLRouter:
    return GraphQLRouter(
        schema, context_getter=get_context, subscription_protocols=[GRAPHQL_WS_PROTOCOL]
    )


graphql_router = get_gql_router()
