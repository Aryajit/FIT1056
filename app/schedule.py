import json
import os
from app.student import StudentUser
from app.teacher import TeacherUser, Course

class ScheduleManager:
    def __init__(self, data_filepath="data/msms.json"):
        self.data_filepath = data_filepath
        self.students = []
        self.teachers = []
        self.courses = []
        self.attendance_log = []  # Initialize attendance log state
        self._load_data()

    def _load_data(self):
        if not os.path.exists(self.data_filepath):
            return

        with open(self.data_filepath, "r") as f:
            data = json.load(f)

        # Load Students into objects
        for s in data.get("students", []):
            self.students.append(StudentUser(s["user_id"], s["name"], s["email"], s["grade_level"]))

        # Load Teachers into objects
        for t in data.get("teachers", []):
            self.teachers.append(TeacherUser(t["user_id"], t["name"], t["email"], t["instrument_specialty"]))

        # Load Courses into objects
        for c in data.get("courses", []):
            self.courses.append(Course(c["course_id"], c["title"], c["teacher_id"]))

        # Load Attendance Log safely using .get()
        self.attendance_log = data.get("attendance", [])

    def _save_data(self):
        data = {
            "students": [s.to_dict() for s in self.students],
            "teachers": [t.to_dict() for t in self.teachers],
            "courses": [c.to_dict() for c in self.courses],
            "attendance": self.attendance_log
        }
        with open(self.data_filepath, "w") as f:
            json.dump(data, f, indent=4)

    def check_in(self, student_id, course_id, date_str):
        """Fragment 3.3: Student check-in method with validation."""
        # Check if student exists
        student = next((s for s in self.students if s.user_id == student_id), None)
        if not student:
            print(f"Error: Student ID {student_id} not found.")
            return False

        # Check if course exists
        course = next((c for c in self.courses if c.course_id == course_id), None)
        if not course:
            print(f"Error: Course ID {course_id} not found.")
            return False

        record = {
            "student_id": student_id,
            "course_id": course_id,
            "date": date_str
        }
        
        self.attendance_log.append(record)
        self._save_data()  # Persist changes immediately
        print(f"Success: {student.name} checked into {course.title}.")
        return True