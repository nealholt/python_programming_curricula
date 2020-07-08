import random

'''
This thing here is like Oregon Trail.
'''

name = input('What is your name, adventurer?')

difficulty = int(input('Choose a difficulty. 1: hard. 2: medium. 3: easy.'))
while difficulty<1 or difficulty>3:
    print('Choose 1, 2, or 3.')
    difficulty = int(input('Choose a difficulty. 1: hard. 2: medium. 3: easy.'))

magnifier = 3

strength = random.randint(difficulty, difficulty*magnifier)
intelligence = random.randint(difficulty, difficulty*magnifier)
dexterity = random.randint(difficulty, difficulty*magnifier)
hp = random.randint(difficulty*magnifier, (difficulty+2)*magnifier)
mana = random.randint(difficulty*magnifier, (difficulty+2)*magnifier)

print(name+' has '+str(hp)+' health and '+str(mana)+' magic.')
print('Your strength is '+str(strength))
print('Your intelligence is '+str(intelligence))
print('Your dexterity is '+str(dexterity))


def getChoice(question):
    choice = int(input(question))
    while not(choice==1 or choice==2 or choice==3):
        choice = int(input(question))
    return choice


x = getChoice('Welcome, '+name+'. Do you dare cross the treacherous sea (1), delve the dangerous dungeon (2), or climb the majestic mountain (3)?')
if x == 1: #sea
    print("A tentacled sea monster rises from the depths and attacks your ship.")
    monster_hp = 10
    while monster_hp>0 and hp>0:
        damage = random.randint(1,5)
        print("\nThe monster looks angry. It slaps you with a tentacle for "+str(damage)+" damage.")
        hp = hp - damage
        x = getChoice('1: Cast a fire spell. 2. Shoot it with an arrow. 3. Stab it with your sword.')
        if x==1:
            if mana < 1:
                print('Your magic is exhausted.')
            else:
                mana = mana - 2
                monster_hp = monster_hp - intelligence
                print('The sea monster writhes in pain.')
        elif x==2:
                monster_hp = monster_hp - int(dexterity/2)
                print('The sea monster is barely bothered by your arrows.')
        else:
            print("The monster's hide is too tough for your sword.")
    if hp<1:
        print("\nThe monster drags you down to a watery grave.")
    else:
        print("\nYou defeat the monster.")
elif x == 2: #dungeon
    print('NOT IMPLEMENTED')
else: #mountain
    print('NOT IMPLEMENTED')

#Score depends on difficulty modifier at the end.
if hp>0:
    score = 100-(strength+intelligence+dexterity)
    print("\nYour score is "+str(score))
    if hp+mana > magnifier*2:
        print('... and you made it look easy.')
else:
    print("\nBetter luck next time.")