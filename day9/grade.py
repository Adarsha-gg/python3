student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades ={}

for score in student_scores:
    student_gradess = student_scores[score]
    if student_gradess > 90:
        student_grades[score] = "Outstanding"
    elif student_gradess > 80:
        student_grades[score] = "Exceeds Expectation"
    elif student_gradess > 70:
        student_grades[score] = "Aceeptable"
    elif student_gradess <= 70:
        student_grades[score] = "Fail"     

print(student_grades)





