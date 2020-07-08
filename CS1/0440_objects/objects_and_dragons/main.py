import dragon, character

#Setup the hero and enemy
name = input("What is your name?  ")
role = input("Are you a wizard, rogue, or warrior?  ")
you = character.Character(name, role)
enemy = dragon.Dragon()
#Play the game
print("You encounter an evil dragon!")
while not enemy.isDead():
    ability = input("Do you attack with 'sword', 'magic', or 'sneak'?  ")
    if ability == "sword":
        you.swingSword(enemy)
    elif ability == "magic":
        you.castSpell(enemy)
    elif ability == "sneak":
        you.sneakAttack(enemy)
    else:
        print("What is '"+ability+"'? You seem confused!")
print("\nYou have vanquished the beast!\n")
