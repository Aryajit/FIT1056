"""
PST3 Main Entry Point (View Layer)
Music School Management System (MSMS)
"""

import sys
import os

# Ensure the app package can be imported regardless of execution path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.schedule import ScheduleManager


def print_menu():
    """Displays the main menu options for the MSMS application."""
    print("\n" + "=" * 45)
    print("   MUSIC SCHOOL MANAGEMENT SYSTEM (PST3)")
    print("=" * 45)
    print("1. View All Students")
    print("2. View All Courses")
    print("3. Check-In Student to Course")
    print("4. Save & Exit")
    print("=" * 45)


def main():
    """Main execution loop for the terminal user interface."""
    # Instantiate the controller layer (loads data from data/msms.json)
    manager = ScheduleManager(data_filepath="data/msms.json")
    
    while True:
        print_menu()
        choice = input("Select an option (1-4): ").strip()
        
        if choice == "1":
            print("\n--- Registered Students ---")
            if not manager.students:
                print("No students currently registered.")
            else:
                for student in manager.students:
                    print(f"ID: {student.user_id} | Name: {student.name} | Level: {getattr(student, 'grade_level', 'N/A')}")
                    
        elif choice == "2":
            print("\n--- Available Courses ---")
            if not manager.courses:
                print("No courses currently available.")
            else:
                for course in manager.courses:
                    title = getattr(course, "title", getattr(course, "name", "Course"))
                    c_id = getattr(course, "course_id", getattr(course, "id", "N/A"))
                    print(f"Course ID: {c_id} | Title: {title}")
                    
        elif choice == "3":
            print("\n--- Student Check-In ---")
            try:
                student_id = int(input("Enter Student ID: ").strip())
                course_id = int(input("Enter Course ID: ").strip())
                
                # Delegate business logic to the ScheduleManager controller
                manager.check_in(student_id, course_id)
            except ValueError:
                print("Error: Invalid input. Please enter numeric IDs.")
                
        elif choice == "4":
            print("\nSaving data and exiting Music School Management System. Goodbye!")
            sys.exit(0)
            
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()