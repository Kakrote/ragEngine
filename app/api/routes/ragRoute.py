from fastapi import APIRouter
from app.schemas.rag_schema import QueryRequest, QueryResponse
from app.services.rag_service import RagService

router = APIRouter()

rag_service = RagService()


@router.post("/query", response_model=QueryResponse)
async def query_rag(payload: QueryRequest):
    answer = await rag_service.query(payload.question)
    return QueryResponse(answer=answer)
