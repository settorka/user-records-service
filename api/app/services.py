from .models import Record

class RecordService:
    """Service layer to handle record operations."""
    
    def __init__(self):
        self.record = Record(attributes={"name": "John Doe", "age": 30, "country": "USA"})

    def get_record(self):
        """Retrieve the current record."""
        return self.record.to_dict()

    def update_record(self, **kwargs):
        """Update the record with new attributes."""
        # Validation example: Ensure age is non-negative
        if "age" in kwargs and kwargs["age"] < 0:
            raise ValueError("Age must be non-negative.")
        self.record.update(**kwargs)
        return {"message": "Record updated successfully"}
