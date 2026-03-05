from fastapi import APIRouter
from app.schemas.rag_schema import (
    QueryRequest,
    QueryResponse,
    IndexRequest,
    IndexResponse,
)
from fastapi import UploadFile, File
from app.utils.pdf_parser import PDFParser
from app.services.rag_service import RagService
from app.services.ingestion_service import IngestionService

router = APIRouter()

rag_service = RagService()
ingestion_service = IngestionService()


@router.post("/query", response_model=QueryResponse)
async def query_rag(payload: QueryRequest):
    answer = await rag_service.query(payload.question)
    return QueryResponse(answer=answer)


@router.post("/index", response_model=IndexResponse)
async def index_document(payload: IndexRequest):
    message = await ingestion_service.index_document(payload.content)
    return IndexResponse(message=message)


@router.post("/index-pdf")
async def index_pdf(file: UploadFile = File(...)):
    parser = PDFParser()

    # Save temporarily
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Extract text
    text = parser.extract_text(file_location)

    # Index using existing service
    message = await ingestion_service.index_document(text)

    return {"message": message}