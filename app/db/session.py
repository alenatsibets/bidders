from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import asynccontextmanager
import os
from dotenv import load_dotenv
import ssl

load_dotenv()
DATABASE_URL = os.getenv("DB_URL")

ssl_context = ssl.create_default_context()
connect_args = {"ssl": ssl_context}

engine = create_async_engine(
    DATABASE_URL, echo=True, connect_args=connect_args
)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()

@asynccontextmanager
async def get_db_session():
    async with async_session() as session:
        yield session
