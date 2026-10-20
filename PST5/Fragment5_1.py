# ... inside ScheduleManager class ...
import csv
import datetime

def record_payment(self, student_id, amount, method):
    """Adds a payment record to the finance log."""
    # Find the student to ensure they exist (optional validation guard)
    student_exists = any(s.id == student_id for s in self.students)
    if not student_exists:
        print(f"Error: Student with ID {student_id} not found.")
        return False

    # Create a payment dictionary with student_id, amount, method, and a timestamp.
    payment_record = {
        "student_id": student_id,
        "amount": amount,
        "method": method,
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    # Append the record to self.finance_log and save the data.
    self.finance_log.append(payment_record)
    self._save_data()
    print(f"Payment of {amount} for student {student_id} recorded.")
    return True

def get_payment_history(self, student_id):
    """Returns a list of all payments for a given student."""
    # Use a list comprehension to filter self.finance_log
    # and return only the records that match the student_id.
    return [p for p in self.finance_log if p['student_id'] == student_id]

def export_report(self, kind, out_path):
    """Exports a log to a CSV file."""
    print(f"Exporting {kind} report to {out_path}...")
    
    # Use an if/elif block to select the correct data list based on 'kind'.
    if kind == "finance":
        data_to_export = self.finance_log
        headers = ["student_id", "amount", "method", "timestamp"]
    elif kind == "attendance":
        data_to_export = getattr(self, "attendance_log", [])
        headers = ["student_id", "course_id", "timestamp"]
    else:
        print("Error: Unknown report type.")
        return False

    # Use Python's 'csv' module to write the data using a DictWriter.
    try:
        with open(out_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            writer.writerows(data_to_export)
        print(f"Successfully exported {kind} report to {out_path}")
        return True
    except Exception as e:
        print(f"Failed to export report: {e}")
        return False

# ... inside ScheduleManager class ...