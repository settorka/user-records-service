from locust import constant
from base_test import APIUser

class SoakTest(APIUser):
    """Simulates a soak test with sustained load."""
    wait_time = constant(2)  # Sustained load with fixed intervals
