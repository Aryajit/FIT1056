# gui/finance_pages.py
import streamlit as st
import pandas as pd

def show_finance_page(manager):
    """Renders the UI for all financial operations."""
    st.header("Finance & Payments")

    # --- Section 1: Record a Payment ---
    st.subheader("Record New Payment")
    with st.form("payment_form"):
        # Create a dictionary mapping student names to their IDs for selection
        student_list = {s.name: s.id for s in manager.students}
        selected_student_name = st.selectbox("Select Student", list(student_list.keys()))
        
        # Create a number input for the payment amount and a text input for the method
        amount = st.number_input("Payment Amount", min_value=0.01, format="%.2f")
        method = st.text_input("Payment Method (e.g., Credit Card, Cash)")
        
        submitted = st.form_submit_button("Record Payment")
        if submitted:
            if student_list:
                student_id = student_list[selected_student_name]
                # Call manager.record_payment() and show a success message
                manager.record_payment(student_id, amount, method)
                st.success(f"Payment of ${amount:.2f} via {method} for {selected_student_name} recorded successfully.")
            else:
                st.warning("No students available to record a payment for.")

    # --- Section 2: View Payment History ---
    st.subheader("View Student Payment History")
    
    if student_list:
        history_student_name = st.selectbox("Select Student to View History", list(student_list.keys()), key="history_select")
        if history_student_name:
            history_student_id = student_list[history_student_name]
            # Call manager.get_payment_history() to fetch records
            history = manager.get_payment_history(history_student_id)
            if history:
                # Convert the list of dictionaries to a pandas DataFrame and display it
                df = pd.DataFrame(history)
                st.dataframe(df, use_container_width=True)
            else:
                st.info("This student has no payment history.")
    else:
        st.info("No students found in the system.")