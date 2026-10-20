# app/student.py
from app.user import User

class StudentUser(User):
    """Represents a student, inheriting from the base User class."""
    def __init__(self, user_id, name, enrolled_course_ids=None):
        # Call the parent class's __init__ method using super()
        super().__init__(user_id, name)
        # Initialize the list of enrolled course IDs
        self.enrolled_course_ids = enrolled_course_ids if enrolled_course_ids is not None else []

    def enroll_course(self, course_id):
        """Enrolls the student in a course if not already enrolled."""
        if course_id not in self.enrolled_course_ids:
            self.enrolled_course_ids.append(course_id)

    def to_dict(self):
        """Converts the StudentUser instance into a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "enrolled_course_ids": self.enrolled_course_ids
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a StudentUser instance from a dictionary."""
        return cls(
            user_id=data.get("id"),
            name=data.get("name"),
            enrolled_course_ids=data.get("enrolled_course_ids", [])
        )