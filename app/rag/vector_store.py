class VectorStore:

    async def similarity_search(self, query: str):
        # fake data — later pgvector search
        return [
            "FastAPI is a modern web framework.",
            "RAG stands for Retrieval Augmented Generation."
        ]
