from locust import HttpUser, task, between
from base_test import BaseFaker, BaseTest

class SpikeTest(BaseTest):
    """Simulates a spike in traffic."""
    wait_time = between(0.1, 0.5)  # Short wait times for spike effect
