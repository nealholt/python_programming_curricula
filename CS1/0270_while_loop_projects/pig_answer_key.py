import random

player1_score = 0
player2_score = 0

ending_score = 100

def takeTurn(safe_score):
    temp_score = 0
    choice = 'r'
    roll = 0
    while roll != 1 and choice != 'h':
        roll = random.randint(1,6)
        if roll == 1:
            print('you rolled 1. lose your turn')
        else:
            temp_score = temp_score + roll
            choice = input('You rolled '+str(roll)+
                "\nYour temporary score is "+str(temp_score)+
                "\nYour safe score is "+str(safe_score)+
                "\nroll (r) or hold (h)?")
    return temp_score

#While no one has won, keep playing
while player1_score < 100 and player2_score < 100:
    player1_score = player1_score + takeTurn(player1_score)
    player2_score = player2_score + takeTurn(player2_score)


if player1_score >= 100:
    print('Player 1 wins!')
else:
    print('Player 2 wins!')
