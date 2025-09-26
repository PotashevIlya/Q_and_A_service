from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.answer import answer_crud
from app.schemas.answer import RetrieveAnswer
from app.api.validators import check_answer_exist


router = APIRouter()


@router.get(
    "/{id}",
    response_model=RetrieveAnswer
)
async def get_answer(
    id: int,
    session: AsyncSession = Depends(get_async_session),
):
    """Получить ответ."""
    return await check_answer_exist(answer_id=id, session=session)


@router.delete(
    "/{id}"
)
async def delete_answer(
    id: int,
    session: AsyncSession = Depends(get_async_session),
) -> str:
    """Удалить ответ."""
    answer = await check_answer_exist(answer_id=id, session=session)
    await answer_crud.remove(db_obj=answer, session=session)
    return f"Ответ с id {id} успешно удалён"
