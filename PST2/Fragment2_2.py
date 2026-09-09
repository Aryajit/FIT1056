# --- Full CRUD for Core Data ---
# Note: We are now working with lists of dictionaries, not lists of objects.

def add_teacher(name, speciality):
    """Adds a teacher dictionary to the data store."""
    # TODO: Get the next teacher ID from app_data['next_teacher_id'].
    teacher_id = app_data['next_teacher_id']
    # Explanation: Retrieves the current unique ID counter from the app_data dictionary[cite: 6].

    # TODO: Create a new teacher dictionary with 'id', 'name', and 'speciality' keys.
    new_teacher = {"id": teacher_id, "name": name, "speciality": speciality}
    # Explanation: Constructs a key-value dictionary representing the teacher record[cite: 6].

    # TODO: Append the new dictionary to the app_data['teachers'] list.
    app_data['teachers'].append(new_teacher)
    # Explanation: Stores the newly created teacher dictionary into the 'teachers' list in app_data[cite: 6].

    # TODO: Increment the 'next_teacher_id' in app_data.
    app_data['next_teacher_id'] += 1
    # Explanation: Increases the ID counter by 1 to maintain unique IDs for subsequent teachers[cite: 6].

    print(f"Core: Teacher '{name}' added.")


def update_teacher(teacher_id, **fields):
    """Finds a teacher by ID and updates their data with provided fields."""
    # TODO: Loop through the app_data['teachers'] list.
    for teacher in app_data['teachers']:
        # TODO: If a teacher's 'id' matches teacher_id:
        if teacher['id'] == teacher_id:
            # Use the .update() method on the teacher dictionary to apply the 'fields'.
            teacher.update(fields)
            # Explanation: Merges key-value updates directly into the matched teacher dictionary[cite: 6].
            
            print(f"Teacher {teacher_id} updated.")
            return
    print(f"Error: Teacher with ID {teacher_id} not found.")


def remove_student(student_id):
    """Removes a student from the data store."""
    # TODO: Find the student dictionary in app_data['students'] with the matching ID.
    # If found, use the .remove() method on the list to delete it.
    # A list comprehension is a clean way to do this:
    initial_length = len(app_data['students'])
    app_data['students'] = [s for s in app_data['students'] if s['id'] != student_id]
    
    if len(app_data['students']) < initial_length:
        print(f"Student {student_id} removed.")
    else:
        print(f"Error: Student with ID {student_id} not found.")
    # Explanation: Rebuilds the student list filtering out the given student ID and confirms deletion if length changed[cite: 6].


# TODO: Implement remove_teacher() and update_student() using the patterns above.
def remove_teacher(teacher_id):
    """Removes a teacher from the data store."""
    initial_length = len(app_data['teachers'])
    app_data['teachers'] = [t for t in app_data['teachers'] if t['id'] != teacher_id]
    
    if len(app_data['teachers']) < initial_length:
        print(f"Teacher {teacher_id} removed.")
    else:
        print(f"Error: Teacher with ID {teacher_id} not found.")
    # Explanation: Filters out the teacher dictionary with the matching ID from app_data['teachers'][cite: 6].


def update_student(student_id, **fields):
    """Finds a student by ID and updates their data with provided fields."""
    for student in app_data['students']:
        if student['id'] == student_id:
            student.update(fields)
            print(f"Student {student_id} updated.")
            return
    print(f"Error: Student with ID {student_id} not found.")
    # Explanation: Iterates through app_data['students'], finds the matching ID, and applies keyword updates via .update()[cite: 6].