from prometheus_client import Counter, Histogram

# Define Prometheus metrics
REQUEST_COUNT = Counter("request_count", "Total number of requests", ["method", "endpoint", "status"])
REQUEST_LATENCY = Histogram("request_latency_seconds", "Request latency in seconds", ["method", "endpoint"])

def record_metrics(method: str, endpoint: str, status: str, latency: float):
    """Record metrics for a request."""
    REQUEST_COUNT.labels(method=method, endpoint=endpoint, status=status).inc()
    REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(latency)
