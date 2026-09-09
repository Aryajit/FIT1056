# --- Main Application ---
def main():
    """Runs the main interactive menu for the receptionist."""
    # Pre-populate some data for easy testing
    add_teacher("Dr. Keys", "Piano")
    add_teacher("Ms. Fret", "Guitar")

    while True:
        print("\n===== Music School Front Desk =====")
        print("1. Register New Student")
        print("2. Enrol Existing Student")
        print("3. Lookup Student or Teacher")
        print("4. (Admin) List all Students")
        print("5. (Admin) List all Teachers")
        print("q. Quit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            # TODO: Prompt for student name and instrument, then call front_desk_register.
            name = input("Enter student name: ")
            instrument = input("Enter instrument to enrol in: ")
            front_desk_register(name, instrument)
            # Explanation: Prompts the user for student name and instrument, then delegates execution to front_desk_register to handle object creation and enrollment[cite: 1, 4].

        elif choice == '2':
            # TODO: Prompt for student ID (as an int) and instrument, then call front_desk_enrol.
            try:
                student_id = int(input("Enter student ID: "))
                instrument = input("Enter instrument to enrol in: ")
                front_desk_enrol(student_id, instrument)
            except ValueError:
                print("Invalid ID. Please enter a number.")
            # Explanation: Prompts for student ID and instrument; wraps ID parsing in a try-except block to catch invalid non-integer inputs gracefully before passing valid arguments to front_desk_enrol[cite: 1, 4].

        elif choice == '3':
            # TODO: Prompt for a search term, then call front_desk_lookup.
            term = input("Enter search term: ")
            front_desk_lookup(term)
            # Explanation: Reads a search string from input and passes it to front_desk_lookup to search across both student and teacher records[cite: 1, 4].

        elif choice == '4':
            list_students()
            # Explanation: Calls list_students to print all student records stored in runtime memory[cite: 1, 4].

        elif choice == '5':
            list_teachers()
            # Explanation: Calls list_teachers to print all teacher records stored in runtime memory[cite: 1, 4].

        elif choice.lower() == 'q':
            print("Exiting program. Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

# --- Program Start ---
if __name__ == "__main__":
    main()