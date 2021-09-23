# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
int_age = int(age)
final_age = 90
left_age = final_age-int_age
left_days = left_age * 365
left_weeks = left_age * 52
left_months = left_age * 12
# print(f"Your age is {int_age} years old, or {months} months, or {weeks} weeks, or {days} days.")
# if we live till 90 years old that means 90 - age
print(f"You have {left_days} days, {left_weeks} weeks, and {left_months} months left.")