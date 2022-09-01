# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
print(student_heights)

#Write your code below this row 👇

#add the list of student heights using the for loop 
#use a variable to count the number of times the loop ran for the length of the list
sum_temp = 0
length_temp = 0
for sum_height in student_heights:
  sum_temp += sum_height
  length_temp += 1

avg_height = sum_temp/length_temp

print(sum_temp)
print(length_temp)
print(int(avg_height))
