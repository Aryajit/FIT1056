from app.schedule import ScheduleManager

def front_desk_daily_roster(manager, day):
    """View function to display daily roster / attendance log."""
    print(f"\n--- Daily Roster for {day} ---")
    records = [rec for rec in manager.attendance_log if rec.get("date") == day]
    
    if not records:
        print("No attendance records found for this date.")
        return

    for rec in records:
        print(f"Student ID: {rec['student_id']} | Course ID: {rec['course_id']}")

def main():
    # Initialize the brain of the application
    manager = ScheduleManager(data_filepath="data/msms.json")

    print("====================================")
    print(" Welcome to Music School Manager ")
    print("====================================")

    # Example Check-In Test
    # Replace these IDs with sample IDs present in your data/msms.json
    print("\nAttempting student check-in...")
    manager.check_in(student_id="S001", course_id="C001", date_str="2026-09-04")

    # Display Daily Roster View
    front_desk_daily_roster(manager, "2026-09-04")

if __name__ == "__main__": 
    main()
    