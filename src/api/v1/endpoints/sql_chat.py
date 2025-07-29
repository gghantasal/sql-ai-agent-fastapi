# src/api/v1/endpoints/sql_chat.py
from fastapi import APIRouter, HTTPException, status
from src.models.chat import ChatRequest, ChatResponse
from src.core.agent import query_sql_agent # <--- This import should now work
from src.utils.logger import logger

router = APIRouter()

@router.post(
    "/ask",
    response_model=ChatResponse,
    summary="Ask the SQL AI Agent a question",
    description="Send a natural language question to the AI agent to query the database and get a natural language answer.",
    status_code=status.HTTP_200_OK
)
async def ask_question(request: ChatRequest):
    logger.info(f"API request received: {request.question}")
    try:
        answer = await query_sql_agent(request.question)
        return ChatResponse(answer=answer)
    except Exception as e:
        logger.exception(f"Error processing request for question: {request.question}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"An internal server error occurred: {e}"
        )