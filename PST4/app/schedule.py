import json
from app.student import StudentUser
# Corrected Import: TeacherUser and Course now come from the same file.
from app.teacher import TeacherUser, Course

class ScheduleManager:
    """The main controller for all business logic and data handling."""
    def __init__(self, data_path="data/msms.json"):
        self.data_path = data_path
        self.students = []
        self.teachers = []
        self.courses = []
        self.next_lesson_id = 1
        self._load_data()

    def _load_data(self):
        """Loads data from the JSON file and populates the object lists."""
        try:
            with open(self.data_path, 'r') as f:
                data = json.load(f)
                
                # Reconstruct StudentUser objects
                for s_dict in data.get('students', []):
                    # Handle from_dict factory method if available, else unpack dictionary
                    if hasattr(StudentUser, 'from_dict'):
                        student = StudentUser.from_dict(s_dict)
                    else:
                        student = StudentUser(**s_dict)
                    self.students.append(student)

                # Reconstruct TeacherUser objects
                for t_dict in data.get('teachers', []):
                    if hasattr(TeacherUser, 'from_dict'):
                        teacher = TeacherUser.from_dict(t_dict)
                    else:
                        teacher = TeacherUser(**t_dict)
                    self.teachers.append(teacher)

                # Reconstruct Course objects
                for c_dict in data.get('courses', []):
                    if hasattr(Course, 'from_dict'):
                        course = Course.from_dict(c_dict)
                    else:
                        course = Course(**c_dict)
                    self.courses.append(course)
                    
        except FileNotFoundError:
            print("Data file not found. Starting with a clean state.")
        except json.JSONDecodeError:
            print("Error decoding JSON file. Starting with empty state.")

    def _save_data(self):
        """Converts object lists back to dictionaries and saves to JSON."""
        students_data = [
            s.to_dict() if hasattr(s, 'to_dict') else s.__dict__ 
            for s in self.students
        ]
        teachers_data = [
            t.to_dict() if hasattr(t, 'to_dict') else t.__dict__ 
            for t in self.teachers
        ]
        courses_data = [
            c.to_dict() if hasattr(c, 'to_dict') else c.__dict__ 
            for c in self.courses
        ]

        data_to_save = {
            "students": students_data,
            "teachers": teachers_data,
            "courses": courses_data
        }

        try:
            with open(self.data_path, 'w') as f:
                json.dump(data_to_save, f, indent=4)
        except Exception as e:
            print(f"Failed to save data to {self.data_path}: {e}")