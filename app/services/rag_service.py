from app.rag.pipeline import RagPipeline


class RagService:

    def __init__(self):
        self.pipeline = RagPipeline()

    async def query(self, question: str) -> str:
        result = await self.pipeline.run(question)
        return result
