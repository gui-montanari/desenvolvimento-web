from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine

from core.configs import settings


engine: AsyncEngine = create_async_engine(settings.DATABASE_URL, echo=False)


async def get_session() -> AsyncSession:
    __async_session = sessionmaker(
        bind=engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autocommit=False,
        autoflush=False,
    )
    session: AsyncSession = __async_session()
    return session


async def create_tables() -> None:
    import models.__all_models
    print('Criando as tabelas no banco de dados')
    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print(f'Tabelas criadas com sucesso.')