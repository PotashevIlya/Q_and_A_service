from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.db import Base


if TYPE_CHECKING:
    from .question import Question


class Answer(Base):
    """Модель ответа."""

    question_id: Mapped[int] = mapped_column(
        ForeignKey("question.id", ondelete="CASCADE"),
        nullable=False
    )
    user_id: Mapped[str] = mapped_column(nullable=False)
    text: Mapped[str] = mapped_column(nullable=False)

    # M-T-O связь к вопросу.
    question: Mapped["Question"] = relationship(
        "Question",
        back_populates="answers"
    )

    def __repr__(self) -> str:
        return f"Ответ. id: {self.id}. Текст: {self.text[:20]}"
