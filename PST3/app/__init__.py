# app/__init__.py
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