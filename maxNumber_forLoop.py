# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# max() function will get the maximum number from the list 
# min() function will get the minmum number from the list
#   but in this case we want to to avoid using this max function
#   we're only using for loop and logic
#   If we move to another lanuage we may not be able to find these
#   functions so we have to use logic and think little to be able
#   to implement these methods

max = 0
for x in student_scores:
    if x > max:
        x = max

print(f"The highest score in the class is: {max}")