import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

userChoice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.'))
print(f"You chose: {userChoice}")
if userChoice == 0:
    print(rock)
elif userChoice == 1:
    print(paper)
elif userChoice == 2:
    print(scissors)
else: 
    print('Invalid entry. Please try again.')
    exit()
computerChoice = random.randint(0,2)
print(f"Computer chose: {computerChoice}")
if computerChoice == 0:
    print(rock)
elif computerChoice == 1:
    print(paper)
elif computerChoice == 2:
    print(scissors)
# Rules of the game:
#   - Rock wins against scissors.
#   - Scissors win against paper.
#   - Paper wins against rock.
# Remember our choices are 0 for Rock, 1 for Paper or 2 for Scissors.

# You win if one these rules apply: 
if (userChoice == 0 and computerChoice == 2) or (userChoice == 2 and computerChoice == 1) or (userChoice == 1 and computerChoice == 0):
    print('You won')
# It's tie if one of these rules apply:
elif (userChoice == computerChoice):
    print('It\'s tie.')
else: 
    print('You lose')