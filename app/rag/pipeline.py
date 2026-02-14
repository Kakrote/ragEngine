from app.rag.retriever import Retriever


class RagPipeline:

    def __init__(self):
        self.retriever = Retriever()

    async def run(self, question: str) -> str:
        # Step 1 — retrieve docs
        docs = await self.retriever.search(question)

        # Step 2 — fake LLM generation (we add real LLM later)
        context = " ".join(docs)

        return f"Generated answer using context: {context}"
