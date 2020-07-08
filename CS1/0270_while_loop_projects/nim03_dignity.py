player1 = input("Player 1, enter your name: ")
player2 = input("Player 2, enter your name: ")

#Piles
a = 5
b = 4
c = 3

def getPileAmount(pile):
    if pile == 'A':
        return a
    elif pile == 'B':
        return b
    else:
        return c

#Current player
cur_player = player1

while a+b+c > 1:
    #Display the piles
    print("A: "+str(a)+"\tB: "+str(b)+"\tC: "+str(c))
    #Get the player's choice
    choice = input(cur_player+", choose a pile: ")
    choice = choice.upper()
    #Cheat protection
    while not(choice in ['A','B','C']) or getPileAmount(choice)==0:
        choice = input("Nice try, "+cur_player+". Choose a pile: ")
        choice = choice.upper()
    amount = int(input("How many to remove from pile "+choice+": "))
    #Cheat protection
    while amount<1 or amount>getPileAmount(choice):
        amount = int(input("Nice try. How many to remove from pile "+choice+": "))
    #Remove the chosen amount from the chosen pile
    if choice=='A':
        a = max(0,a-amount)
    elif choice=='B':
        b = max(0,b-amount)
    else:
        c = max(0,c-amount)
    #Switch players
    if cur_player==player1:
        cur_player=player2
    else:
        cur_player=player1

#Announce the winner
if a+b+c == 0:
    print(cur_player+", there are no counters left, so you WIN!")
else:
    #Switch players
    if cur_player==player1:
        cur_player=player2
    else:
        cur_player=player1
    print(cur_player+", there are is one counter left, so you WIN!")
