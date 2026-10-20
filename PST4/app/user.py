# app/user.py

class User:
    """A base class for all users in the system."""
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name

    def to_dict(self):
        """Converts the User instance into a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a User instance from a dictionary."""
        return cls(
            user_id=data.get("id"),
            name=data.get("name")
        )

    def __repr__(self):
        return f"<{self.__class__.__name__}(id='{self.id}', name='{self.name}')>"