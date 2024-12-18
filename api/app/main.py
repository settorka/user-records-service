import time
from fastapi import FastAPI, HTTPException
from prometheus_client import generate_latest
from starlette.responses import Response
from pydantic import BaseModel
from .services import RecordService
from .middleware import LoggingMiddleware
from .metrics import record_metrics

app = FastAPI()

# Add middleware
app.add_middleware(LoggingMiddleware)

# Initialize service
record_service = RecordService()

class UpdateRecordRequest(BaseModel):
    """Pydantic model for updating the record."""
    attributes: dict

@app.get("/api/v1/record")
async def get_record():
    """Endpoint to get the current record."""
    start_time = time.time()
    try:
        result = record_service.get_record()
        status = "200"
    except Exception as e:
        status = "500"
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        latency = time.time() - start_time
        record_metrics(method="GET", endpoint="/api/v1/record", status=status, latency=latency)
    return result

@app.put("/api/v1/record")
async def update_record(request: UpdateRecordRequest):
    """Endpoint to update the record."""
    start_time = time.time()
    try:
        result = record_service.update_record(**request.attributes)
        status = "200"
    except ValueError as e:
        status = "400"
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        status = "500"
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        latency = time.time() - start_time
        record_metrics(method="PUT", endpoint="/api/v1/record", status=status, latency=latency)
    return result

@app.get("/metrics")
def metrics():
    """Endpoint for Prometheus to scrape metrics."""
    return Response(generate_latest(), media_type="text/plain")
