def student_grades():
    student_grades = {}
    average_grade = 0

    while len(student_grades) < 3:
        subject = input("List a school subject: ")
        grade = input("What was the grade in that subject: ")

        student_grades[subject] = int(grade)

    grade_line = 'You had these grades:'

    for key in student_grades:
        grade_line = grade_line + ' ' + key + ': ' + str(student_grades[key])

    print(grade_line)

    for value in student_grades.values():
        average_grade += value

    average_grade = average_grade/len(student_grades)

    print(f'Your average was {average_grade:.2f}')


student_grades()
