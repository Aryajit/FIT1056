from app.user import User

class StudentUser(User):
    def __init__(self, user_id, name, email, grade_level):
        super().__init__(user_id, name, email)
        self.grade_level = grade_level

    def to_dict(self):
        data = super().to_dict()
        data["grade_level"] = self.grade_level
        return data