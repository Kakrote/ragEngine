# RAG Engine - Python Backend

A FastAPI-based Retrieval-Augmented Generation (RAG) system powered by Google's Gemini AI.

## Features

- 🤖 Question-answering using RAG pipeline
- 📄 Document indexing with vector embeddings
- 📚 PDF file processing and indexing
- 🔍 Semantic search with pgvector
- ⚡ Async operations for better performance
- 🔄 Retry logic for API rate limits

## Tech Stack

- **FastAPI**: Modern web framework
- **Google Gemini**: AI embeddings and text generation
- **PostgreSQL + pgvector**: Vector database for semantic search
- **SQLAlchemy**: Async ORM
- **pypdf**: PDF text extraction

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Set up environment variables
echo "GEMINI_API_KEY=your_api_key_here" > .env

# Run the server
uvicorn app.main:app --reload --port 8000
```

## API Endpoints

### Health Check
```
GET /rag/health
```

### Query RAG System
```
POST /rag/query
{
  "question": "Your question here"
}
```

### Index Document
```
POST /rag/index
{
  "content": "Document text to index"
}
```

### Index PDF
```
POST /rag/index-pdf
FormData: file (PDF)
```

## Environment Variables

```env
GEMINI_API_KEY=your_gemini_api_key
DATABASE_URL=postgresql+asyncpg://user:password@localhost/ragdb
```

## Project Structure

```
app/
├── api/
│   ├── route.py              # Main API router
│   └── routes/
│       ├── healthRoute.py    # Health check endpoint
│       └── ragRoute.py       # RAG endpoints
├── core/                     # Core configurations
├── db/
│   ├── models.py            # Database models
│   └── session.py           # Database session
├── rag/
│   ├── chunking.py          # Text chunking logic
│   ├── pipeline.py          # RAG pipeline
│   ├── retriever.py         # Document retrieval
│   └── vector_store.py      # Vector operations
├── schemas/
│   ├── base.py              # Base schemas
│   └── rag_schema.py        # RAG request/response schemas
├── services/
│   ├── embedding_service.py # Gemini embeddings
│   ├── ingestion_service.py # Document ingestion
│   ├── llm_service.py       # Gemini text generation
│   └── rag_service.py       # Main RAG service
├── utils/
│   └── pdf_parser.py        # PDF parsing utilities
└── main.py                   # Application entry point
```

## Development

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run with auto-reload
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## For more information, see [CONNECTION_GUIDE.md](../CONNECTION_GUIDE.md)
