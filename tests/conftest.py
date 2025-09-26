import pytest
from fastapi.testclient import TestClient
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.core.db import get_async_session, Base
from app.models import Question, Answer


@pytest.fixture(scope="function")
async def test_engine():
    """Создаём тестовый движок и таблицы для in-memory SQLite."""
    engine = create_async_engine(
        "sqlite+aiosqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )

    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    yield engine

    await engine.dispose()


@pytest.fixture(scope="function")
async def test_session(test_engine):
    """Создаём тестовую сессию с БД."""
    async with AsyncSession(test_engine) as session:
        yield session


@pytest.fixture(scope="function")
async def test_client(test_engine):
    """Создаём тестового клиента с изолированной БД"""

    AsyncTestSessionLocal = sessionmaker(
        test_engine, class_=AsyncSession, expire_on_commit=False
    )

    async def override_get_async_session():
        async with AsyncTestSessionLocal() as session:
            yield session

    app.dependency_overrides[get_async_session] = override_get_async_session

    with TestClient(app) as client:
        yield client

    app.dependency_overrides.clear()


@pytest.fixture(scope="function")
async def test_data(test_session):
    """Создаём тестовые данные в изолированной БД"""

    test_question = Question(text="Тестовый вопрос")
    test_session.add(test_question)
    await test_session.commit()
    await test_session.refresh(test_question)

    test_answer = Answer(
        id=1,
        text="Тестовый ответ",
        question_id=test_question.id,
        user_id="test_uid"
    )
    test_session.add(test_answer)
    await test_session.commit()
    await test_session.refresh(test_answer)
