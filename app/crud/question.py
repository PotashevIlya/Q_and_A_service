from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession

from app.crud.base import CRUDBase
from app.models import Question


class QuestionCRUD(CRUDBase):
    """CRUD для работы с моделью Question."""

    async def get_by_id(
            self,
            obj_id: int,
            session: AsyncSession
    ):
        db_obj = await session.execute(
            select(self.model)
            .options(
                selectinload(self.model.answers)
            )
            .where(
                self.model.id == obj_id
            )
        )
        return db_obj.scalars().first()


question_crud = QuestionCRUD(Question)
