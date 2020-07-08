import random

def getRandom():
    r = random.random()
    if r<0.3333:
        return 'rock'
    elif r<0.66666:
        return 'scissors'
    else:
        return 'paper'


computer_choice = getRandom()
user_choice = input('Choose rock, paper, or scissors.')
while not (user_choice in ['rock', 'paper', 'scissors']):
    user_choice = input('Choose rock, paper, or scissors.')

print("You\t\t\tComputer")
print(user_choice+"\tvs\t"+computer_choice)

if user_choice == computer_choice:
    print('Tie!')
elif (user_choice=='rock' and computer_choice=='paper') or\
(user_choice=='scissors' and computer_choice=='rock') or\
(user_choice=='paper' and computer_choice=='scissors'):
    print('you lose')
else:
    print('You win!')
