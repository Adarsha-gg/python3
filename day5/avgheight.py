
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total = 0
item = 0

for i in student_heights:
    total=total + i
for z in student_heights:
    item+=1    
avg=total/item
avg =round(avg)
print(avg)

