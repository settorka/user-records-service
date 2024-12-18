from faker import Faker
from random import sample, randint
from locust import HttpUser, TaskSet, task, between

class BaseFaker:
    """Base class for generating fake attributes."""
    def __init__(self):
        self.faker = Faker()
    
    def generate_attributes(self):
        """Generate a dictionary of potential attributes."""
        return {
            "name": self.faker.name(),
            "age": self.faker.random_int(min=18, max=80),
            "country": self.faker.country(),
            "email": self.faker.email(),
            "job": self.faker.job(),
            "net_worth": self.faker.random_int(min=1000, max=1000000),
            "favorite_color": self.faker.color_name(),
            "hobby": self.faker.word(),
        }

class BaseTest(TaskSet):
    """Base class for testing API with dynamic updates."""
    faker_instance = BaseFaker()

    def generate_update_payload(self):
        """Randomize the number of attributes in the PUT request."""
        all_attributes = self.faker_instance.generate_attributes()
        # Randomly select 1 to N attributes
        num_attributes = randint(1, len(all_attributes))
        selected_attributes = dict(sample(all_attributes.items(), num_attributes))
        return {"attributes": selected_attributes}

    @task
    def get_record(self):
        """Simulate GET request to retrieve the record."""
        self.client.get("/api/v1/record")

    @task
    def put_record(self):
        """Simulate PUT request to update the record."""
        payload = self.generate_update_payload()
        self.client.put("/api/v1/record", json=payload)


class APIUser(HttpUser):
    """Base user for API tests."""
    tasks = [BaseTest]
    wait_time = between(1, 2)  # Simulate users waiting between requests
