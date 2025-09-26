from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Answer


class AnswerCRUD(CRUDBase):
    """CRUD для работы с моделью Answer."""

    async def create(
            self,
            obj_in,
            question_id: int,
            session: AsyncSession,
    ):
        obj_in_data = obj_in.model_dump()
        obj_in_data["question_id"] = question_id
        db_obj = self.model(**obj_in_data)
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj


answer_crud = AnswerCRUD(Answer)
