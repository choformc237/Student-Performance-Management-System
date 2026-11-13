"""
Student Performance Management System
For: Chi McDonald

A simple system to manage student records and analyze performance.
"""

import json
from datetime import datetime

class StudentPerformanceSystem:
    def __init__(self):
        self.students = {}
    
    def add_student(self, student_id, name, course):
        """Add a new student"""
        self.students[student_id] = {
            'name': name,
            'course': course,
            'grades': [],
            'created_at': datetime.now().isoformat()
        }
        print(f"Student {name} added successfully.")
    
    def add_grade(self, student_id, subject, score):
        """Add a grade for a student"""
        if student_id not in self.students:
            print("Student not found.")
            return
        self.students[student_id]['grades'].append({
            'subject': subject,
            'score': score,
            'date': datetime.now().isoformat()
        })
        print(f"Grade added for {subject}: {score}")
    
    def get_average(self, student_id):
        """Calculate average score for a student"""
        if student_id not in self.students:
            return None
        grades = self.students[student_id]['grades']
        if not grades:
            return 0
        return sum(g['score'] for g in grades) / len(grades)
    
    def predict_performance(self, student_id):
        """Simple performance prediction based on average"""
        avg = self.get_average(student_id)
        if avg is None:
            return "Student not found"
        if avg >= 80:
            return "Excellent - High performance expected"
        elif avg >= 60:
            return "Good - Steady performance expected"
        elif avg >= 40:
            return "Average - Needs improvement"
        else:
            return "At Risk - Requires intervention"
    
    def display_all(self):
        """Display all students"""
        for sid, info in self.students.items():
            avg = self.get_average(sid)
            print(f"ID: {sid}, Name: {info['name']}, Avg: {avg:.2f if avg else 0}, Prediction: {self.predict_performance(sid)}")

def main():
    system = StudentPerformanceSystem()
    
    # Demo data
    system.add_student("S001", "Chi McDonald", "Computer Science")
    system.add_grade("S001", "Python", 85)
    system.add_grade("S001", "Data Structures", 78)
    system.add_grade("S001", "Database", 92)
    
    print("\n--- Student Performance Report ---")
    system.display_all()
    print(f"\nPrediction for Chi McDonald: {system.predict_performance('S001')}")

if __name__ == "__main__":
    main()
