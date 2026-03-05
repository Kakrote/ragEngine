import google.generativeai as genai
import os
import asyncio
import time
from google.api_core.exceptions import ResourceExhausted


class EmbeddingService:

    def __init__(self):
        genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

    async def generate(self, text: str, max_retries: int = 5):
        for attempt in range(max_retries):
            try:
                response = genai.embed_content(
                    model="models/gemini-embedding-001",
                    content=text
                )
                return response["embedding"]
            except ResourceExhausted as e:
                if attempt < max_retries - 1:
                    wait_time = min(2 ** attempt * 3, 60)
                    print(f"Rate limited, retrying in {wait_time}s (attempt {attempt + 1}/{max_retries})")
                    await asyncio.sleep(wait_time)
                else:
                    raise