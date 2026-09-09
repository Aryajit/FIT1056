# --- Main Application Loop ---
def main():
    """Main function to run the MSMS application."""
    load_data() # Load all data from file at startup.

    while True:
        print("\n===== MSMS v2 (Persistent) =====")
        print("1. Check-in Student")
        print("2. Print Student Card")
        print("3. Update Teacher Info")
        print("4. Remove Student")
        print("q. Quit and Save")
        
        choice = input("Enter your choice: ")
        
        made_change = False # A flag to track if we need to save
        if choice == '1':
            # TODO: Get student_id and course_id from user, then call check_in().
            student_id = input("Enter student ID (e.g., S001): ").strip()
            course_id = input("Enter course ID (e.g., C001): ").strip()
            check_in(student_id, course_id)
            made_change = True
            # Explanation: Collects student and course IDs from user input and executes check_in, setting made_change to True to trigger auto-saving.

        elif choice == '2':
            # TODO: Get student_id, then call print_student_card().
            student_id = input("Enter student ID to print card: ").strip()
            print_student_card(student_id)
            pass # No change made, so no save needed
            # Explanation: Obtains student ID and calls print_student_card to output an ID badge text file without modifying persistent app state.

        elif choice == '3':
            # TODO: Get teacher_id and new details, then call update_teacher().
            try:
                teacher_id = int(input("Enter teacher ID: ").strip())
                new_speciality = input("Enter new speciality (leave blank to skip): ").strip()
                if new_speciality:
                    update_teacher(teacher_id, speciality=new_speciality)
                    made_change = True
                else:
                    print("No details provided for update.")
            except ValueError:
                print("Invalid input! Teacher ID must be an integer.")
            # Explanation: Prompts for teacher ID and optional new speciality, applying changes via update_teacher if inputs are valid.

        elif choice == '4':
            # TODO: Get student_id, then call remove_student().
            student_id = input("Enter student ID to remove: ").strip()
            remove_student(student_id)
            made_change = True
            # Explanation: Reads the target student ID and calls remove_student to delete the record, setting made_change to True to trigger an immediate save.

        elif choice.lower() == 'q':
            print("Saving final changes and exiting.")
            break
        else:
            print("Invalid choice.")
            
        if made_change:
            save_data() # Save the data immediately after any change.

    save_data() # One final save on exit.

# --- Program Start ---
if __name__ == "__main__":
    main()