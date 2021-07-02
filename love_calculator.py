# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Hints : 
# 1. The lower() function changes all the letters in a string to lower case.
# 2. The count() function will give you the number of times a letter occurs in a string.

# T R U E
score = 0
name1_lower = name1.lower()
T = name1_lower.count('t')
R = name1_lower.count('r')
U = name1_lower.count('u')
E = name1_lower.count('e')
if T > 0 or R > 0 or U > 0 or E > 0:
    score = T + R+ U + E
# print(f"T occurs {name1_lower.count('t')} times")
# print(f"R occurs {name1_lower.count('r')} times")
# print(f"U occurs {name1_lower.count('u')} times")
# print(f"E occurs {name1_lower.count('e')} times")
# print (f"Total = {score}")

# L O V E
score2=0
L = name1_lower.count('l')
O = name1_lower.count('o')
V = name1_lower.count('v')
E2 = name1_lower.count('e')
if L > 0 or O > 0 or V > 0 or E2 > 0:
    score2 = L + O + V + E2
# print(f"L occurs {name1_lower.count('l')} times")
# print(f"O occurs {name1_lower.count('o')} times")
# print(f"V occurs {name1_lower.count('v')} times")
# print(f"E occurs {name1_lower.count('e')} times")
# print (f"Total = {score2}")

print(f"Your score is {score}{score2}")