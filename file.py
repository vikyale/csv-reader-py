
import csv

student_list = []

with open('student_data.csv', 'r') as file:
    writer = csv.DictReader(file)

    for row in writer:
        student_list.append(row)

print(student_list)


average_age = sum(int(student['age']) for student in student_list) / len(student_list)
average_grade = sum(float(student['grade']) for student in student_list) / len(student_list)

print(f"Average Age: {average_age:.2f}")
print(f"Average Grade: {average_grade:.2f}")