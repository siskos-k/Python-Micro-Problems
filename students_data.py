import random

def generate_student_grades():
    # Create a list of subjects
    subjects = ['Math', 'Science', 'English', 'History']

    # Generate a dictionary of student grades
    student_grades = {}

    for _ in range(5):  # To create grades for 5 students
        name = f"Student{_}"
        student_grades[name] = {}

        # Ensure each student has at least 3 grades per subject
        for subject in subjects:
            grades = [random.randint(60, 100) for _ in range(3)]
            student_grades[name][subject] = grades

    return student_grades


result = generate_student_grades()
print(result)
