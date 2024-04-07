from random import *

userinput = input('Enter your choice (rock, paper, or scissor): ')
userinput = userinput.lower()

# Validate user input
while userinput not in ['rock', 'paper', 'scissor']:
    print("Invalid input. Please enter 'rock', 'paper', or 'scissor'.")
    userinput = input('Enter your choice: ')
    userinput = userinput.lower()

n = randint(0, 2)
choices = ['rock', 'paper', 'scissor']
computerChoice = choices[n]
print(f'Computer choice is {computerChoice}')
print(f'Your choice is {userinput}')

if userinput == computerChoice:
    print('Draw')
elif userinput == 'rock' and computerChoice == 'paper':
    print('Computer wins')
elif userinput == 'paper' and computerChoice == 'scissor':
    print('Computer wins')
elif userinput == 'scissor' and computerChoice == 'rock':
    print('Computer wins')
else:
    print('You Win')