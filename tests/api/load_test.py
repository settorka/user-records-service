from locust import constant
from base_test import APIUser

class LoadTest(APIUser):
    """Simulates a load test with a steady number of users."""
    wait_time = constant(1)  # Steady load with constant wait time
