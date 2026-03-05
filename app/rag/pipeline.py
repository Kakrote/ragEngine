from app.rag.retriever import Retriever
from app.services.llm_service import LLMService


class RagPipeline:

    def __init__(self):
        self.retriever = Retriever()
        self.llm = LLMService()

    async def run(self, question: str) -> str:
        # 1️⃣ Retrieve similar documents
        docs = await self.retriever.search(question)

        # 2️⃣ Merge context
        context = "\n".join(docs)

        # 3️⃣ Generate response using Gemini
        answer = await self.llm.generate(question, context)

        return answer