# pst4/gui/roster_pages.py
import streamlit as st
import pandas as pd

def show_roster_page(manager):
    """Renders the daily roster and check-in functionality."""
    st.header("Daily Roster")

    # --- View Roster Section ---
    day = st.selectbox("Select a day", ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
    
    # Fetch schedule data for the selected day from manager
    if hasattr(manager, "get_daily_roster"):
        daily_classes = manager.get_daily_roster(day)
    else:
        # Fallback filter directly from manager.courses if helper method doesn't exist
        daily_classes = [c for c in manager.courses if getattr(c, "day", "").capitalize() == day]

    if daily_classes:
        # Convert objects to a dictionary list for Pandas DataFrame display
        roster_data = []
        for c in daily_classes:
            roster_data.append({
                "Course ID": getattr(c, "id", "N/A"),
                "Course Name": getattr(c, "name", "N/A"),
                "Time": getattr(c, "time", "N/A"),
                "Teacher": getattr(c.teacher, "name", "Unassigned") if hasattr(c, "teacher") and c.teacher else "Unassigned",
                "Enrolled Students": len(getattr(c, "students", []))
            })
        df = pd.DataFrame(roster_data)
        st.dataframe(df, use_container_width=True)
    else:
        st.info(f"No classes scheduled for {day}.")

    st.divider()

    # --- Student Check-in Section ---
    st.subheader("Student Check-in")
    
    # Safely retrieve student and course lists from the manager
    students = getattr(manager, "students", [])
    courses = getattr(manager, "courses", [])

    if not students or not courses:
        st.warning("Please ensure there are students and courses registered in the system before checking in.")
        return

    with st.form("check_in_form"):
        # Populate the dropdowns dynamically using name -> id dictionaries
        student_list = {s.name: s.id for s in students}
        course_list = {c.name: c.id for c in courses}
        
        selected_student_name = st.selectbox("Select Student", list(student_list.keys()))
        selected_course_name = st.selectbox("Select Course", list(course_list.keys()))
        
        submitted = st.form_submit_button("Check-in Student")

        if submitted:
            # Convert selected names back to IDs
            student_id = student_list[selected_student_name]
            course_id = course_list[selected_course_name]

            # Execute check-in via ScheduleManager
            result = manager.check_in(student_id, course_id)

            # Handle both boolean and tuple (success, message) return types from PST3
            if isinstance(result, tuple):
                success, message = result
            else:
                success, message = result, f"Checked in {selected_student_name} for {selected_course_name}!"

            if success:
                st.success(message)
            else:
                st.error("Check-in failed. Verify if the student is enrolled in this course.")