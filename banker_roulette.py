# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
# First Method is using random.choice
#random.choice is widely used function that will help you pick a random item in a list.
# print(random.choice(names))
# Second method is using "len" function again to get the number or count that list 

randomPicker = random.randint(1,len(names)-1)
Person = names[randomPicker]
# print(len(names)-1)
# print(names[randomPicker])
print(f"{Person} is going tp biu the meal today.")