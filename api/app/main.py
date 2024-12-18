import time
from fastapi import FastAPI, Request, HTTPException
from prometheus_client import generate_latest
from starlette.responses import Response
from .services import RecordService
from .middleware import LoggingMiddleware
from .metrics import record_metrics, REQUEST_COUNT, REQUEST_LATENCY

app = FastAPI()

# Add middleware
app.add_middleware(LoggingMiddleware)

# Initialize service
record_service = RecordService()

@app.get("/api/v1/record")
async def get_record():
    """Endpoint to get the record."""
    start_time = time.time()
    try:
        result = record_service.get_record()
        status = "200"
    except Exception as e:
        status = "500"
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        latency = time.time() - start_time
        record_metrics(method="GET", endpoint="/record", status=status, latency=latency)
    return result

@app.put("/api/v1/record")
async def update_record(name: str, age: int, country: str):
    """Endpoint to update the record."""
    start_time = time.time()
    try:
        result = record_service.update_record(name=name, age=age, country=country)
        status = "200"
    except ValueError as e:
        status = "400"
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        status = "500"
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        latency = time.time() - start_time
        record_metrics(method="PUT", endpoint="/record", status=status, latency=latency)
    return result

@app.get("/metrics")
def metrics():
    """Endpoint for Prometheus to scrape metrics."""
    return Response(generate_latest(), media_type="text/plain")
