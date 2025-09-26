from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field


class CreateAnswer(BaseModel):
    """Схема запроса на создание ответа."""

    user_id: str
    text: str = Field(
        ...,
        min_length=10,
        examples=["Ваш ответ. Минимум 10 символов."]
    )


class RetrieveAnswer(CreateAnswer):
    """Схема на отображение объекта ответа."""

    id: int
    question_id: int
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
