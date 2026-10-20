"""
PST2 - Fragment 2.3: Student Check-In & Student Card Generation
Music School Management System (MSMS)
"""

import datetime
from Fragment2_1 import save_data


def check_in_student(data, student_id, course_id):
    """
    Validates student and course existence, logs an attendance timestamp,
    and saves the updated data back to msms.json.
    """
    # 1. Search for student
    student = next((s for s in data.get("students", []) if s["user_id"] == student_id), None)
    if not student:
        print(f"Error: Student ID {student_id} not found.")
        return False

    # 2. Search for course
    course = next((c for c in data.get("courses", []) if c["course_id"] == course_id), None)
    if not course:
        print(f"Error: Course ID {course_id} not found.")
        return False

    # 3. Record attendance check-in entry
    timestamp = datetime.datetime.now().isoformat()
    check_in_record = {
        "student_id": student_id,
        "course_id": course_id,
        "timestamp": timestamp
    }

    if "attendance" not in data:
        data["attendance"] = []
    
    data["attendance"].append(check_in_record)

    # 4. Save to persistent file
    save_data(data)
    print(f"Success: {student['name']} checked into {course['title']} at {timestamp}.")
    return True


def generate_student_card(student_data, filename=None):
    """
    Generates a formatted text file representing a Student ID card badge.
    """
    student_id = student_data.get("user_id", "N/A")
    name = student_data.get("name", "Unknown")
    email = student_data.get("email", "N/A")
    grade = student_data.get("grade_level", "N/A")

    card_content = f"""===================================
    MUSIC SCHOOL STUDENT CARD
===================================
ID          : {student_id}
Name        : {name}
Email       : {email}
Grade Level : {grade}
===================================
"""

    if filename is None:
        filename = f"student_card_{student_id}.txt"

    with open(filename, "w") as f:
        f.write(card_content)

    print(f"Student card successfully generated: {filename}")
    return filename


if __name__ == "__main__":
    # Test stub data
    sample_data = {
        "students": [{"user_id": 1, "name": "Alice Smith", "email": "alice@example.com", "grade_level": "Beginner"}],
        "courses": [{"course_id": 101, "title": "Piano Basics"}],
        "attendance": []
    }
    
    # Run test card generation
    generate_student_card(sample_data["students"][0])