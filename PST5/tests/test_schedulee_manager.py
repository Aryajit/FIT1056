# tests/test_schedule_manager.py
import pytest
import os
from app.schedule import ScheduleManager

# A pytest fixture creates a clean environment for each test function.
@pytest.fixture
def fresh_manager():
    """Creates a fresh ScheduleManager instance using a temporary test data file."""
    test_file = "test_data.json"
    # ARRANGE: Ensure no old test file exists.
    if os.path.exists(test_file):
        os.remove(test_file)
    manager = ScheduleManager(data_path=test_file)
    yield manager
    # TEARDOWN: Clean up the test file after tests complete.
    if os.path.exists(test_file):
        os.remove(test_file)

def test_create_course(fresh_manager):
    # ARRANGE: We have a fresh manager from the fixture.
    # ACT: Call the method we want to test.
    fresh_manager.create_course("Beginner Piano", "Piano", 1)
    # ASSERT: Check if the outcome is what we expect.
    assert len(fresh_manager.courses) == 1
    assert fresh_manager.courses[0].name == "Beginner Piano"

def test_record_payment_and_history(fresh_manager):
    # ARRANGE: Add a dummy student or mock the student check if required.
    # ACT: Record a payment for that student.
    student_id_to_test = 1
    fresh_manager.record_payment(student_id_to_test, 100.00, "Credit Card")
    
    # ACT 2: Get the payment history.
    history = fresh_manager.get_payment_history(student_id_to_test)

    # ASSERT: Check the results.
    assert len(history) == 1
    assert history[0]['amount'] == 100.00
    assert history[0]['method'] == "Credit Card"
    
def test_get_payment_history_no_results(fresh_manager):
    # ARRANGE: Query for a student ID that has no recorded payments.
    non_existent_student_id = 999
    
    # ACT: Retrieve the payment history.
    history = fresh_manager.get_payment_history(non_existent_student_id)
    
    # ASSERT: Verify that the result is an empty list.
    assert isinstance(history, list)
    assert len(history) == 0

# tests/test_schedule_manager.py