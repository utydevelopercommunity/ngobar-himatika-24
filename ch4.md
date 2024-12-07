Problem
Create a function called student_performance_tracker that analyzes student test scores. The function should:

1. Accept a dictionary of student names and their test scores
2. Calculate each student's average score
3. Determine a letter grade for each student
4. Identify the highest and lowest scoring students
5. Provide an overall class performance summary

Sample Input:
student_scores = {
    'Alice': [85, 92, 88],
    'Bob': [75, 78, 80],
    'Charlie': [90, 95, 92]
}


Expected Output:
{
    'individual_scores': {
        'Alice': {'average': 88.33, 'letter_grade': 'B'},
        'Bob': {'average': 77.67, 'letter_grade': 'C'},
        'Charlie': {'average': 92.33, 'letter_grade': 'A'}
    },
    'class_summary': {
        'highest_scorer': 'Charlie',
        'lowest_scorer': 'Bob',
        'class_average': 86.11,
        'top_performers': ['Charlie', 'Alice']
    }
}
