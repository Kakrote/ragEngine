from app.rag.vector_store import VectorStore


class Retriever:

    def __init__(self):
        self.vector_store = VectorStore()

    async def search(self, query: str):
        results = await self.vector_store.similarity_search(query)
        return results
