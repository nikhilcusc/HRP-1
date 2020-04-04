'''
HackerLand University has the following grading policy:

Every student receives a grade  in the inclusive range from 0  to 100 .
Any grade less than 40  is a failing grade.
Sam is a professor at the university and likes to round each student's grade according to these rules:

If the difference between the grade and the next multiple of 5 is less than 3, round  up to the next multiple of 5.
If the value of grade is less than 38, no rounding occurs as the result will still be a failing grade.
'''

def gradingStudents(grades):
    for grade in grades:
        gm5 = grade%5
        #print("grade : ",grade, '\t gm5 :',gm5)
        if grade > 37 and (gm5==3 or gm5==4):
            grade = (grade+(5-gm5))
        print(grade)
    return


grades = [4, 73, 67, 38, 33, 84, 95, 99, 96]
gradingStudents(grades)

