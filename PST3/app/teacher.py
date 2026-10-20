#TeacherUser(User): Inherits from User and adds a speciality attribute (e.g., "Piano", "Guitar").

#Course: Represents a class offered by the school. Holds course_id, title, teacher_id, enrolled_student_ids, and lessons.

from app.user import User

class TeacherUser(User):
    """Represents a teacher, inheriting from the base User class."""
    # TODO: Implement the TeacherUser class, inheriting from User.
    # It should have an additional 'speciality' attribute in its __init__.
    def __init__(self, user_id, name, email="", speciality=""):
        super().__init__(user_id, name)
        # Explanation: Invokes User parent constructor to set user_id and name.
        self.email = email
        self.speciality = speciality
        # Explanation: Assigns email and speciality attributes specific to teacher profiles.

    def to_dict(self):
        """Converts the TeacherUser instance into a dictionary for JSON serialization."""
        return {
            "user_id": self.user_id,
            "name": self.name,
            "email": self.email,
            "instrument_specialty": self.speciality
        }

class Course:
    """Represents a single course offered by the school, linked to a teacher."""
    def __init__(self, course_id, name, teacher_id, instrument=""):
        self.course_id = course_id
        self.title = name
        self.instrument = instrument
        self.teacher_id = teacher_id
        
        # TODO: Initialize two empty lists: 'enrolled_student_ids' and 'lessons'.
        self.enrolled_student_ids = []
        self.lessons = [] # This will hold lesson dictionaries
        # Explanation: Pre-allocates empty lists to track student enrollments and scheduled lesson sessions.

    def to_dict(self):
        """Converts the Course instance into a dictionary for JSON serialization."""
        return {
            "course_id": self.course_id,
            "title": self.title,
            "instrument": self.instrument,
            "teacher_id": self.teacher_id,
            "enrolled_student_ids": self.enrolled_student_ids,
            "lessons": self.lessons
        }