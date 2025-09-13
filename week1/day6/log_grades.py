def student_grades():
    file_path = "grade_log.txt"

    student_grades = {}
    average_grade = 0

    while len(student_grades) < 3:
        subject = input("List a school subject: ")
        grade = input("What was the grade in that subject: ")

        student_grades[subject] = int(grade)

    grade_line = 'You had these grades:\n'

    for key in student_grades:
        grade_line = grade_line + ' ' + key + ': ' + str(student_grades[key]) + '\n'

    for value in student_grades.values():
        average_grade += value

    average_grade = average_grade/len(student_grades)

    with open(file_path, 'a') as file_object:
        file_object.write(grade_line + '\n' + f'Your average was {average_grade:.2f}\n\n')

student_grades()
