# app/teacher.py
from app.user import User

class TeacherUser(User):
    """Represents a teacher, inheriting from the base User class."""
    def __init__(self, user_id, name, speciality):
        super().__init__(user_id, name)
        self.speciality = speciality

    def to_dict(self):
        """Converts the TeacherUser instance into a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "speciality": self.speciality
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a TeacherUser instance from a dictionary."""
        return cls(
            user_id=data.get("id"),
            name=data.get("name"),
            speciality=data.get("speciality")
        )


class Course:
    """Represents a single course offered by the school, linked to a teacher."""
    def __init__(self, course_id, name, instrument, teacher_id, enrolled_student_ids=None, lessons=None):
        self.id = course_id
        self.name = name
        self.instrument = instrument
        self.teacher_id = teacher_id
        # Initialize empty lists for enrolled students and lesson schedule dictionaries
        self.enrolled_student_ids = enrolled_student_ids if enrolled_student_ids is not None else []
        self.lessons = lessons if lessons is not None else []

    def enroll_student(self, student_id):
        """Enrolls a student in the course if not already enrolled."""
        if student_id not in self.enrolled_student_ids:
            self.enrolled_student_ids.append(student_id)

    def add_lesson(self, day, time):
        """Adds a scheduled lesson dictionary to the course."""
        lesson = {"day": day, "time": time}
        self.lessons.append(lesson)

    def to_dict(self):
        """Converts the Course instance into a dictionary for JSON serialization."""
        return {
            "id": self.id,
            "name": self.name,
            "instrument": self.instrument,
            "teacher_id": self.teacher_id,
            "enrolled_student_ids": self.enrolled_student_ids,
            "lessons": self.lessons
        }

    @classmethod
    def from_dict(cls, data):
        """Creates a Course instance from a dictionary."""
        return cls(
            course_id=data.get("id"),
            name=data.get("name"),
            instrument=data.get("instrument"),
            teacher_id=data.get("teacher_id"),
            enrolled_student_ids=data.get("enrolled_student_ids", []),
            lessons=data.get("lessons", [])
        )