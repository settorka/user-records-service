from locust import HttpUser, task, between, LoadShape
from base_test import APIUser

class StressTest(APIUser):
    """Simulates a stress test by gradually increasing load."""
    wait_time = between(1, 3)

class StepLoadShape(LoadShape):
    """Custom step load shape for stress testing."""

    step_users = 30
    step_time = 10
    max_users = 5000

    def tick(self):
        run_time = self.get_run_time()
        if run_time > self.max_users * self.step_time:
            return None
        current_step = run_time // self.step_time
        return (self.step_users * current_step, self.step_time)
