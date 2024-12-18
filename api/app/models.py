from typing import Any, Dict
from dataclasses import dataclass, field

@dataclass
class Record:
    """Dynamic and flexible Record model."""
    attributes: Dict[str, Any] = field(default_factory=dict)

    def update(self, **kwargs) -> None:
        """Update the record with new fields or values."""
        for key, value in kwargs.items():
            self.attributes[key] = value

    def get(self, key: str) -> Any:
        """Get the value of a specific attribute."""
        if key not in self.attributes:
            raise KeyError(f"Key '{key}' does not exist in the record.")
        return self.attributes[key]

    def to_dict(self) -> Dict[str, Any]:
        """Return the record as a dictionary."""
        return self.attributes
