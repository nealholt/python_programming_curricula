def ai(sticks_left):
    if sticks_left%4 == 0:
        return 3
    elif (sticks_left+1)%4 == 0:
        return 2
    else:
        return 1

print("Welcome to the game of pickup sticks")
sticks_left = 20
playerturn = True
pickup = 0
while sticks_left > 0:
    if playerturn:
        print("It is Player1's turn")
        pickup = int(input("How many sticks will you pick up? 1, 2, or 3"))
        while pickup>3 or pickup<1:
            print("Invalid choice please choose again.")
            pickup = int(input("How many sticks will you pick up? 1, 2, or 3"))
    else:
        print("It is Computer's turn")
        pickup = ai(sticks_left)
        print("\nThe Computer has picked up "+str(pickup)+" sticks\n")
    sticks_left = sticks_left - pickup
    playerturn = not playerturn
    print("There are "+str(sticks_left)+" sticks left, pick one, two, or three. If you pick up the last stick you lose.")

print("Game Over")
if playerturn:
    print("Player 1 has won")
else:
    print("Computer has won")