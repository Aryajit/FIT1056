class User:
    """A base class for all users in the system."""
    def __init__(self, user_id, name, email=""):
        self.user_id = user_id
        self.name = name
        self.email = email
        # Explanation: Standardizes unique user identification across derived classes (StudentUser, TeacherUser) with optional contact info.

    def to_dict(self):
        """Converts the User instance into a JSON-serializable dictionary."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email
        }
        # Explanation: Exposes a base dictionary representation for inheritance and simple JSON persistence.