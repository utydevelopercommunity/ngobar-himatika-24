Problem:
Write a Python function called process_student_grades that takes a list of dictionaries representing students and their course grades. Each dictionary contains a student's name and a list of their grades. The function should:

Calculate the average grade for each student
Create a new list of students who have an average grade above 85
Sort this new list by average grade in descending order
Return a list of tuples containing (student name, average grade)

Here's a sample input to work with:
pythonCopystudents = [
    {"name": "Alice", "grades": [92, 85, 88, 90]},
    {"name": "Bob", "grades": [75, 80, 82, 79]},
    {"name": "Charlie", "grades": [88, 92, 95, 90]},
    {"name": "David", "grades": [70, 75, 80, 65]}
]

