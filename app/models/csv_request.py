from pydantic import BaseModel
from typing import Any


class CSVRequest(BaseModel):
    items: list[dict[str, Any]]