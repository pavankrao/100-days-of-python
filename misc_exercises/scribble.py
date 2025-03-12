import random

student_names = [
    'Alex',
    'Beth',
    'Caroline',
    'Dave',
    'Eleanor',
    'Freddie'
]

# student_scores = {
#     student: random.randint(1,100) for student in student_names
# }

student_scores = {
    'Alex': 83, 
    'Beth': 14, 
    'Caroline': 36, 
    'Dave': 90, 
    'Eleanor': 82, 
    'Freddie': 27
}

passing_students = {
    student:score for student, score in student_scores.items() if score >= 60
}

print(passing_students)