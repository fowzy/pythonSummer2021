# 🚨 Don't change the code below 👇
from typing import Collection


row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Example: 23 means column 2 and row 3 or we could say position[column=2][row=3]
# So we have to insert "X" in that position 
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']
# so let's say we're going to read it from the "map" var which is a comibiation of row1+row2+row3
# row[1][insert the x in element number 0 as an example
# map [row[0][1],row[1][2],row[2][3]]
# before we get a start it we have to learn how to read the input and split the two numbers :D
# ex: 23 which is according to the docs 2 is the number of the list[column] and 3 is the number of row

column = int(position[0])
row = int(position[1])
print(column, "+" , row)
map[row-1][column-1] = "x"
#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")