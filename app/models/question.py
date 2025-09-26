from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


if TYPE_CHECKING:
    from .answer import Answer


class Question(Base):
    """Модель вопроса."""

    text: Mapped[str] = mapped_column(nullable=False)

    # O-T-M связь к ответу.
    answers: Mapped[list["Answer"]] = relationship(
        "Answer",
        back_populates="question",
        cascade="all, delete-orphan",
        passive_deletes=True
    )

    def __repr__(self) -> str:
        return f"Вопрос. id: {self.id}. Текст: {self.text[:20]}"
