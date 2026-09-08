# Music School Management System (MSMS) - PST1

## Overview
This is an in-memory prototype of the Music School Management System (MSMS) built for FIT1056.

## Structure
- **Data Models:** `Student` and `Teacher` classes.
- **Helper Functions:** Functions to add teachers, list data, and perform searches.
- **Front Desk Functions:** High-level functions for student registration, enrollment, and lookups.
- **Main Loop:** An interactive command-line interface.

# Music School Management System (MSMS) - PST2

## Description
PST2 introduces JSON file persistence (`msms.json`) to store application state permanently, alongside full CRUD operations and receptionist tools.

## How to Run
Run `python pst2_main.py` in the terminal or VS Code environment.

## Design Choices
- Handled missing database files gracefully with fallback initialization.
- Used flexible `**kwargs` for clean model field updates.

# Music School Management System (MSMS) - PST3

## Overview
This project is an Object-Oriented Software Engineering redesign of the Music School Management System (MSMS) built for FIT1056. It refactors a procedural script into a modular Model-View-Controller (MVC) architecture.

## Architecture & Structure
- **`app/user.py`**: Base `User` model containing shared attributes (`user_id`, `name`, `email`).
- **`app/student.py`**: `StudentUser` subclass inheriting from `User`.
- **`app/teacher.py`**: `TeacherUser` subclass inheriting from `User`, and the `Course` model.
- **`app/schedule.py`**: Controller layer (`ScheduleManager`) managing state, JSON persistence (`data/msms.json`), and core business logic (`check_in`).
- **`data/msms.json`**: Persistent JSON database storing students, teachers, courses, and attendance logs.
- **`main.py`**: View layer entry point handling execution flow and output formatting.

## Setup & Running
1. Clone the repository and checkout the `individual` branch:
   ```bash
   git checkout individual