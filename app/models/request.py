from pydantic import BaseModel, HttpUrl


class ExtractionRequest(BaseModel):
    url: HttpUrl
    prompt: str