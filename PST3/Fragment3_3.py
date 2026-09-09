# --- HELPER METHODS REQUIRED BY FRAGMENT 3.3 ---

    def find_student_by_id(self, student_id):
        """Helper method to locate a StudentUser instance by ID."""
        for student in self.students:
            if getattr(student, "user_id", getattr(student, "id", None)) == student_id:
                return student
        return None

    def find_course_by_id(self, course_id):
        """Helper method to locate a Course instance by ID."""
        for course in self.courses:
            if getattr(course, "course_id", getattr(course, "id", None)) == course_id:
                return course
        return None

    # --- FRAGMENT 3.3 IMPLEMENTATION ---

    def check_in(self, student_id, course_id):
        """Records a student's attendance for a course after validation."""
        # Validate that both the student and course exist using the helper methods
        student = self.find_student_by_id(student_id)
        course = self.find_course_by_id(course_id)
        
        if not student or not course:
            print("Error: Check-in failed. Invalid Student or Course ID.")
            return False
            
        timestamp = datetime.datetime.now().isoformat()
        check_in_record = {
            "student_id": student_id, 
            "course_id": course_id, 
            "timestamp": timestamp
        }
        
        # Append to attendance_log and immediately save to disk
        self.attendance_log.append(check_in_record)
        self._save_data()
        
        course_title = getattr(course, "title", getattr(course, "name", "Course"))
        print(f"Success: Student {student.name} checked into {course_title}.")
        return True