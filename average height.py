student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
sum=0
for i in student_heights:
    sum=i+sum
students=0
for i in student_heights:
    students += 1
average=sum/len(student_heights)
average=(round(average))
print(f"total height = {sum}")
print(f"number of students = {students}")
print(f"average height = {average}")

  