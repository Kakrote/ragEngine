from sqlalchemy import select
from app.db.session import AsyncSessionLocal
from app.db.models import Document
from app.services.embedding_service import EmbeddingService


class VectorStore:

    def __init__(self):
        self.embedding_service = EmbeddingService()

    async def similarity_search(self, query: str, k: int = 3):
        query_embedding = await self.embedding_service.generate(query)

        async with AsyncSessionLocal() as session:
            stmt = (
                select(Document)
                .order_by(Document.embedding.l2_distance(query_embedding))
                .limit(k)
            )

            result = await session.execute(stmt)
            documents = result.scalars().all()

        return [doc.content for doc in documents]