# MSMS.py - The In-Memory Prototype

# --- Data Models ---
class Student:
    """A blueprint for student objects. Holds their info."""
    def __init__(self, student_id, name):
        self.id = student_id
        self.name = name
        # TODO: Initialize an empty list called 'enrolled_in' to store instrument names.
        self.enrolled_in = []
        # Explanation: Creates an empty list attribute on the instance to store string names 
        # of instruments/courses the student enrolls in over time.

class Teacher:
    """A blueprint for teacher objects."""
    def __init__(self, teacher_id, name, speciality):
        # TODO: Assign all three parameters (teacher_id, name, speciality)
        # to instance variables (e.g., self.id = teacher_id).
        self.id = teacher_id
        self.name = name
        self.speciality = speciality
        # Explanation: Binds the constructor's parameters to instance attributes on 'self' 
        # so each Teacher object uniquely stores its own ID, full name, and teaching field.

# --- In-Memory Databases ---
# TODO: Create the global data stores.
student_db = []
# Explanation: Initializes a global list to store all created Student objects as temporary records during runtime.

teacher_db = []
# Explanation: Initializes a global list to store all created Teacher objects during runtime.

next_student_id = 1
# Explanation: A global counter starting at 1 to auto-assign unique integer IDs to new students.

next_teacher_id = 1
# Explanation: A global counter starting at 1 to auto-assign unique integer IDs to new teachers.