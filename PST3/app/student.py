#Role: Inherits from User using super().__init__(user_id, name).

# Key Attributes: Adds grade_level and an empty list self.enrolled_course_ids = [].

#Key Methods:

#enroll(course_id): Appends a course ID to the student's enrollment list.

# to_dict(): Exports student-specific fields along with inherited user fields to a dictionary.

from app.user import User

class StudentUser(User):
    def __init__(self, user_id, name, email, grade_level):
        super().__init__(user_id, name, email)
        self.grade_level = grade_level

    def to_dict(self):
        data = super().to_dict()
        data["grade_level"] = self.grade_level
        return data