from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
import traceback

from app.agent.engine import IntelliScoutEngine
from app.exporter.csv_exporter import CSVExporter
from app.models.request import ExtractionRequest
from app.models.csv_request import CSVRequest

router = APIRouter(tags=["Extraction"])

engine = IntelliScoutEngine()
exporter = CSVExporter()


@router.post("/extract")
def extract(request: ExtractionRequest):

    try:

        items = engine.extract(
            url=str(request.url),
            prompt=request.prompt,
        )

        return {
            "items": items
        }

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )


@router.post("/extract/csv")
def extract_csv(request: CSVRequest):

    try:

        csv_file = exporter.export(request.items)

        return FileResponse(
            path=csv_file,
            filename="extracted_data.csv",
            media_type="text/csv",
        )

    except Exception as e:

        traceback.print_exc()

        raise HTTPException(
            status_code=500,
            detail=str(e),
        )