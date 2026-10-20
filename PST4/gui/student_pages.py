# pst4/gui/student_pages.py
import streamlit as st

def show_student_management_page(manager):
    """Renders all components for the student management page."""
    st.header("Student Management")

    # --- Search / Filter Section ---
    st.subheader("Find a Student")
    search_query = st.text_input("Search by Name or Instrument", placeholder="Type student name or instrument...")
    
    # Retrieve student list safely from manager
    students = getattr(manager, "students", [])
    
    if students:
        # Filter students based on search input
        if search_query.strip():
            filtered_students = [
                s for s in students 
                if search_query.lower() in getattr(s, "name", "").lower() or 
                   search_query.lower() in getattr(s, "instrument", "").lower()
            ]
        else:
            filtered_students = students

        if filtered_students:
            student_data = []
            for s in filtered_students:
                student_data.append({
                    "ID": getattr(s, "id", "N/A"),
                    "Name": getattr(s, "name", "N/A"),
                    "Instrument": getattr(s, "instrument", "N/A"),
                    "Enrolled Courses": len(getattr(s, "enrolled_courses", []))
                })
            st.dataframe(student_data, use_container_width=True)
        else:
            st.info(f"No students found matching '{search_query}'.")
    else:
        st.info("No students registered in the system yet.")

    st.divider()

    # --- Registration Section ---
    st.subheader("Register New Student")
    with st.form("registration_form"):
        reg_name = st.text_input("New Student Name")
        reg_instrument = st.text_input("First Instrument")
        submitted = st.form_submit_button("Register Student")
        
        if submitted:
            # Check for blank name or instrument inputs
            if reg_name.strip() and reg_instrument.strip():
                new_student = manager.register_new_student(reg_name.strip(), reg_instrument.strip())
                if new_student:
                    student_id = getattr(new_student, "id", "")
                    id_msg = f" (ID: {student_id})" if student_id else ""
                    st.success(f"Successfully registered {reg_name}{id_msg}!")
                    st.balloons()
                else:
                    st.error(f"Could not register student. A teacher for {reg_instrument} might not be available.")
            else:
                st.warning("Please enter both a name and an instrument.")