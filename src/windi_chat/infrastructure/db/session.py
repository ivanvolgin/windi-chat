from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from windi_chat.core.settings import settings

engine = create_async_engine(settings.DATABASE_URI, echo=True)
AsyncSessionFactory = async_sessionmaker(engine, expire_on_commit=False)