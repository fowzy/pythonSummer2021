# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# In order to count the number of the elements that "student_heights" have we have to run a for loop
# We can't use these two functions:  len() + sum()
# We need to calculate the avg of the heights using for loops
# We have to make a loop that can read our list
#   in the same time we have to set a var = 0 and everytime you read one item you add +1 to that value "var"
#   It's basically counting...
count = 0
total=0
for x in student_heights:
    total+=x
    count+=1
# count the numbers of the heights entry
# print(f"The total count :{count}")

# Total of the heights in the classroom
# print(f"The total of the heights are: {total}")

# Calculate the average
avg=round(total/count)
print(f"Average height in the class room is: {avg}")

#Write your code below this row 👇


