from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from .answer import RetrieveAnswer


class CreateQuestion(BaseModel):
    """Схема запроса на создание вопроса."""

    text: str = Field(
        ...,
        min_length=10,
        examples=["Ваш вопрос. Минимум 10 символов."]
    )


class RetrieveQuestion(CreateQuestion):
    """Схема на отображение объекта вопроса."""

    id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)


class RetrieveQuestionWithAnswers(RetrieveQuestion):
    """Схема на отображение объекта вопроса c ответами."""

    answers: list[RetrieveAnswer]
