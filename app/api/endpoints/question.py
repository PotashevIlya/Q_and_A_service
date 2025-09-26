from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.question import question_crud
from app.crud.answer import answer_crud
from app.schemas.question import CreateQuestion, RetrieveQuestion, RetrieveQuestionWithAnswers
from app.schemas.answer import CreateAnswer, RetrieveAnswer
from app.api.validators import check_question_exist


router = APIRouter()


@router.post(
    "/",
    response_model=RetrieveQuestion,
)
async def create_question(
    request: CreateQuestion,
    session: AsyncSession = Depends(get_async_session),
):
    """Создать вопрос."""
    new_question = await question_crud.create(
        obj_in=request,
        session=session
    )
    return new_question


@router.get(
    "/",
    response_model=list[RetrieveQuestion]
)
async def get_all_questions(
    session: AsyncSession = Depends(get_async_session),
):
    """Получить все вопросы."""
    return await question_crud.get_multi(session=session)


@router.get(
    "/{id}",
    response_model=RetrieveQuestionWithAnswers
)
async def get_question_and_answers(
    id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """Получить вопрос и ответы на него."""
    return await check_question_exist(question_id=id, session=session)


@router.delete(
    "/{id}",
)
async def delete_question(
    id: int,
    session: AsyncSession = Depends(get_async_session),
) -> str:
    """Удалить вопрос и ответы к нему."""
    question = await check_question_exist(
        question_id=id, session=session
    )
    await question_crud.remove(db_obj=question, session=session)
    return f"Вопрос с id {id} успешно удалён"


@router.post(
    "/{id}/answers",
    response_model=RetrieveAnswer,
)
async def create_answer(
    id: int,
    request: CreateAnswer,
    session: AsyncSession = Depends(get_async_session),
):
    """Создать ответ на вопрос."""
    question = await check_question_exist(
        question_id=id, session=session
    )
    return await answer_crud.create(
        obj_in=request,
        question_id=question.id,
        session=session
    )
