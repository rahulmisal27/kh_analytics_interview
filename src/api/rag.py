from core.requests import QuestionRequest, AnswerResponse
from fastapi import APIRouter
from utils.rag_utils import retrieve_chunks, generate_answers

answer_router = APIRouter()


@answer_router.post("/answer_question", response_model=AnswerResponse)
def answer_question(request: QuestionRequest):
    chunks = retrieve_chunks(request.question)
    contexts = "\n".join([chunk.entity.get("text") for chunk in chunks[0]])
    final_answer = generate_answers(contexts, request.question)
    print("Final Answer:", final_answer)
    return AnswerResponse(answer=final_answer)
