from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.models import Question, Answer
from app.crud.question import question_crud
from app.crud.answer import answer_crud


async def check_question_exist(
        question_id: int,
        session: AsyncSession
) -> Question:
    question = await question_crud.get_by_id(
        obj_id=question_id,
        session=session
    )
    if not question:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Вопроса с id {question_id} не существует"
        )
    return question


async def check_answer_exist(
    answer_id: int,
    session: AsyncSession
) -> Answer:
    answer = await answer_crud.get_by_id(
        obj_id=answer_id,
        session=session
    )
    if not answer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Ответа с id {answer_id} не существует"
        )
    return answer
