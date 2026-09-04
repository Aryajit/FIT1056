import json
import os

# Global application state
app_data = {
    "teachers": [],
    "students": [],
    "attendance": [],
    "next_teacher_id": 1,
    "next_student_id": 1
}

def load_data(path="msms.json"):
    """Loads JSON data into app_data. If missing, initializes default structure."""
    global app_data
    if os.path.exists(path):
        try:
            with open(path, "r") as file:
                app_data = json.load(file)
            print("Data successfully loaded.")
        except json.JSONDecodeError:
            print("Error reading JSON file. Starting with default data.")
    else:
        print("No existing data file found. Initializing new database.")

def save_data(path="msms.json"):
    """Saves app_data dictionary to the specified JSON file."""
    try:
        with open(path, "w") as file:
            json.dump(app_data, file, indent=4)
        print("Data saved successfully.")
    except Exception as e:
        print(f"Error saving data: {e}")

        # --- TEACHER CRUD ---

def add_teacher(name, instrument):
    """Creates and adds a new teacher."""
    teacher_id = app_data["next_teacher_id"]
    teacher = {
        "id": teacher_id,
        "name": name,
        "instrument": instrument
    }
    app_data["teachers"].append(teacher)
    app_data["next_teacher_id"] += 1
    print(f"Teacher '{name}' added with ID {teacher_id}.")

def update_teacher(teacher_id, **fields):
    """Updates specified fields for a teacher matching teacher_id."""
    for teacher in app_data["teachers"]:
        if teacher["id"] == teacher_id:
            for key, value in fields.items():
                if key in teacher:
                    teacher[key] = value
            print(f"Teacher ID {teacher_id} updated successfully.")
            return True
    print(f"Teacher ID {teacher_id} not found.")
    return False

def remove_teacher(teacher_id):
    """Deletes a teacher by ID."""
    initial_len = len(app_data["teachers"])
    app_data["teachers"] = [t for t in app_data["teachers"] if t["id"] != teacher_id]
    if len(app_data["teachers"]) < initial_len:
        print(f"Teacher ID {teacher_id} removed.")
        return True
    print(f"Teacher ID {teacher_id} not found.")
    return False

# --- STUDENT CRUD ---

def add_student(name, instrument):
    """Creates and adds a new student."""
    student_id = app_data["next_student_id"]
    student = {
        "id": student_id,
        "name": name,
        "instrument": instrument
    }
    app_data["students"].append(student)
    app_data["next_student_id"] += 1
    print(f"Student '{name}' added with ID {student_id}.")

def update_student(student_id, **fields):
    """Updates specified fields for a student matching student_id."""
    for student in app_data["students"]:
        if student["id"] == student_id:
            for key, value in fields.items():
                if key in student:
                    student[key] = value
            print(f"Student ID {student_id} updated successfully.")
            return True
    print(f"Student ID {student_id} not found.")
    return False

def remove_student(student_id):
    """Deletes a student by ID."""
    initial_len = len(app_data["students"])
    app_data["students"] = [s for s in app_data["students"] if s["id"] != student_id]
    if len(app_data["students"]) < initial_len:
        print(f"Student ID {student_id} removed.")
        return True
    print(f"Student ID {student_id} not found.")
    return False