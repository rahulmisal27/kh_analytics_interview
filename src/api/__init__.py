from fastapi import APIRouter
from api.rag import answer_router
from api.discount import discount_router

router = APIRouter()

router.include_router(answer_router, tags=["RAG"])
router.include_router(discount_router, tags=["Discount"])
