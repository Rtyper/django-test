from dataclasses import dataclass, field
from datetime import date, datetime
from typing import List


# JSON Schema for GigGroup and Event structures
GIG_GROUP_JSON_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "name": {
                "type": "string"
            },
            "description": {
                "type": "string"
            },
            "important": {
                "type": "boolean"
            },
            "events": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string"
                        },
                        "location": {
                            "type": "string"
                        },
                        "address": {
                            "type": "string"
                        },
                        "date": {
                            "type": "string",
                            "pattern": "^\\d{4}-\\d{2}-\\d{2}$",
                            "description": "Date in YYYY-MM-DD format"
                        }
                    },
                    "required": ["name", "location", "address", "date"]
                }
            }
        },
        "required": ["name", "description", "important", "events"]
    }
}


@dataclass
class Event:
    """Represents a single event/gig."""
    name: str
    location: str
    address: str
    date: date
    
    def __str__(self):
        return f"{self.name} - {self.date}"


@dataclass
class GigGroup:
    """Represents a group of related gig events."""
    name: str
    description: str
    important: bool = False
    events: List[Event] = field(default_factory=list)
    
    def __str__(self):
        return self.name
    
    @classmethod
    def from_json_data(cls, json_data):
        """Create GigGroup from JSON data."""
        events = [
            Event(
                name=event_data['name'],
                location=event_data['location'],
                address=event_data['address'],
                date=datetime.strptime(event_data['date'], '%Y-%m-%d').date()
            )
            for event_data in json_data.get('events', [])
        ]
        
        return cls(
            name=json_data['name'],
            description=json_data['description'],
            important=json_data.get('important', False),
            events=events
        )

