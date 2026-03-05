from app.services.embedding_service import EmbeddingService
from app.db.session import AsyncSessionLocal
from app.db.models import Document
from app.rag.chunking import TextChunker


class IngestionService:

    def __init__(self):
        self.embedding_service = EmbeddingService()
        self.chunker = TextChunker()

    async def index_document(self, content: str):

        chunks = self.chunker.split(content)

        async with AsyncSessionLocal() as session:
            for chunk in chunks:
                embedding = await self.embedding_service.generate(chunk)

                doc = Document(
                    content=chunk,
                    embedding=embedding
                )
                session.add(doc)

            await session.commit()

        return f"{len(chunks)} chunks indexed successfully"