from pydantic import BaseModel
from typing import List


class DiscountRequest(BaseModel):
    user_id: str
    product_ids: List[str]


class DiscountResponse(BaseModel):
    discount_percentage: List[float]


class QuestionRequest(BaseModel):
    question: str


class AnswerResponse(BaseModel):
    answer: str
