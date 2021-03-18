# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores \n").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
max = 0
for student in student_scores:
  if student > max:
    max = student
print(f"The highest score in the class is: {max}")
