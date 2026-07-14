import os

from dotenv import load_dotenv
from google import genai

from app.llm.base import BaseLLM

load_dotenv()


class OpenAIClient(BaseLLM):

    def __init__(self):

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError("OPENAI_API_KEY not found in .env")

        self.client = genai.Client(api_key=api_key)

        # Read model from .env
        self.model = os.getenv(
            "GEMINI_MODEL",
            "models/gemini-flash-latest"
        )

    def generate(
        self,
        system: str,
        user: str,
    ) -> str:

        response = self.client.models.generate_content(
            model=self.model,
            contents=f"{system}\n\n{user}"
        )

        return response.text