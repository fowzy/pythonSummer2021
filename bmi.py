# 🚨 Don't change the code below 👇
height = input("enter your height in m: ") 
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# bmi = int(weight)/(float(height)/float(height))
f_height = float(height)
f_weight = float(weight)
bmi = int((f_weight/(f_height*f_height)))
print(bmi)
