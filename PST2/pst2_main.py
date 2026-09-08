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

def check_in(student_id, course_id, timestamp=None):
    """Records a student attendance check-in."""
    if timestamp is None:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    student = next((s for s in app_data["students"] if s["id"] == student_id), None)
    if not student:
        print(f"Check-in failed: Student ID {student_id} does not exist.")
        return False

    record = {
        "student_id": student_id,
        "course_id": course_id,
        "timestamp": timestamp
    }
    app_data["attendance"].append(record)
    print(f"Checked in Student ID {student_id} for course '{course_id}'.")
    return True

def print_student_card(student_id):
    """Generates a text-based physical student card file."""
    student = next((s for s in app_data["students"] if s["id"] == student_id), None)
    if not student:
        print(f"Cannot print card: Student ID {student_id} not found.")
        return False

    card_content = (
        "========================================\n"
        "         MUSIC SCHOOL STUDENT CARD      \n"
        "========================================\n"
        f" ID:         {student['id']}\n"
        f" Name:       {student['name']}\n"
        f" Instrument: {student['instrument']}\n"
        "========================================"
    )
    
    filename = f"student_card_{student_id}.txt"
    with open(filename, "w") as f:
        f.write(card_content)
    
    print(f"Card successfully exported to '{filename}'.")
    return True

def main():
    load_data()  # Auto-loads data on boot

    while True:
        print("\n--- Music School Management System (PST2) ---")
        print("1. Add Teacher")
        print("2. Update Teacher")
        print("3. Remove Teacher")
        print("4. Add Student")
        print("5. Update Student")
        print("6. Remove Student")
        print("7. Student Check-in")
        print("8. Print Student Card")
        print("9. Exit")

        choice = input("Select an option (1-9): ").strip()

        if choice == "1":
            name = input("Enter teacher name: ")
            inst = input("Enter instrument: ")
            add_teacher(name, inst)
            save_data()[cite: 1]

        elif choice == "2":
            t_id = int(input("Enter teacher ID: "))
            name = input("New name (leave blank to skip): ")
            inst = input("New instrument (leave blank to skip): ")
            updates = {}
            if name: updates["name"] = name
            if inst: updates["instrument"] = inst
            update_teacher(t_id, **updates)
            save_data()[cite: 1]

        elif choice == "3":
            t_id = int(input("Enter teacher ID to remove: "))
            remove_teacher(t_id)
            save_data()[cite: 1]

        elif choice == "4":
            name = input("Enter student name: ")
            inst = input("Enter instrument: ")
            add_student(name, inst)
            save_data()[cite: 1]

        elif choice == "5":
            s_id = int(input("Enter student ID: "))
            name = input("New name (leave blank to skip): ")
            inst = input("New instrument (leave blank to skip): ")
            updates = {}
            if name: updates["name"] = name
            if inst: updates["instrument"] = inst
            update_student(s_id, **updates)
            save_data()[cite: 1]

        elif choice == "6":
            s_id = int(input("Enter student ID to remove: "))
            remove_student(s_id)
            save_data()[cite: 1]

        elif choice == "7":
            s_id = int(input("Enter student ID: "))
            c_id = input("Enter course ID: ")
            check_in(s_id, c_id)
            save_data()[cite: 1]

        elif choice == "8":
            s_id = int(input("Enter student ID to print card: "))
            print_student_card(s_id)

        elif choice == "9":
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Try again.")

if __name__ == "__main__":
    main()