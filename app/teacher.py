from app.user import User

class TeacherUser(User):
    def __init__(self, user_id, name, email, instrument_specialty):
        super().__init__(user_id, name, email)
        self.instrument_specialty = instrument_specialty

    def to_dict(self):
        data = super().to_dict()
        data["instrument_specialty"] = self.instrument_specialty
        return data


class Course:
    def __init__(self, course_id, title, teacher_id):
        self.course_id = course_id
        self.title = title
        self.teacher_id = teacher_id

    def to_dict(self):
        return {
            "course_id": self.course_id,
            "title": self.title,
            "teacher_id": self.teacher_id
        }