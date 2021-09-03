print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
answer4q1 = input('You\'r at cross road. Where do you want to go? Type "left" or "right"\n').lower()

if answer4q1 == 'right':
    print('Fall into a hole. Game over')
    exit()
elif answer4q1 == 'left':
    # Continue in the game
    answer4q2 = input('You came to a a lake. There is an island in the middle of the lake. Type \"wait" to wait for a boat. Type "swim" to swim accross.\n').lower()
    if answer4q2 == 'wait':
        answer4q3 = input('You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?\n').lower()
        if answer4q3 == 'red':
            print('Burned by fire. Game over')
            exit()
        elif answer4q3 == 'blue':
            print('Eaten by beasts. Game over.')
            exit()
        elif answer4q3 == 'yellow':
            print('You won!')
            exit()
        else:
            print('Game over.')
            exit()
    else:
        print('You enter a room of beasts. Game Over.')
        exit()
else:
    game_over = input ('Invalid entry. Please try again: ')

