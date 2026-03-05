import google.generativeai as genai
import os


class LLMService:

    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel("gemini-3-flash-preview")

    async def generate(self, question: str, context: str) -> str:
        prompt = f"""
        You are a helpful AI assistant.

        Use ONLY the provided context to answer the question.
        If the answer is not in the context, say you don't know.

        Context:
        {context}

        Question:
        {question}

        Answer:
        """

        response = self.model.generate_content(prompt)
        return response.text