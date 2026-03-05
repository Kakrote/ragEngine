from pydantic import BaseModel


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str


class IndexRequest(BaseModel):
    content: str


class IndexResponse(BaseModel):
    message: str