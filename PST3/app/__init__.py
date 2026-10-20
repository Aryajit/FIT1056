# app/__init__.py
#Role: The parent class for any person in the system.

#Key Code Concept: Uses standard __init__ to store user_id, name, and email.

# to_dict() Method: Converts the Python object instance into a plain dictionary so it can easily be saved into JSON later.
"""
App Package Initialization for Music School Management System (MSMS v3).
Exposes core model classes and controller for easy import access.
"""

from app.user import User
from app.student import StudentUser
from app.teacher import TeacherUser, Course
from app.schedule import ScheduleManager

__all__ = [
    "User",
    "StudentUser",
    "TeacherUser",
    "Course",
    "ScheduleManager"
]