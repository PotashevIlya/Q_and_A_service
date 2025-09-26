from fastapi import APIRouter

from app.api.endpoints import answer_router, question_router

main_router = APIRouter()

main_router.include_router(
    question_router,
    prefix="/questions",
    tags=["Questions"]
)

main_router.include_router(
    answer_router,
    prefix="/answers",
    tags=["Answers"]
)