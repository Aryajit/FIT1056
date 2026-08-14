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