from windi_chat.infrastructure.db.session import AsyncSessionFactory

from sqlalchemy.ext.asyncio import AsyncSession

async def get_session() -> AsyncSession:
    async with AsyncSessionFactory() as session:
        yield session
