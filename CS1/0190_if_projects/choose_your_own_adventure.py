name = input('What is your name, adventurer?')

def getChoice(question):
    choice = int(input(question))
    while not(choice==1 or choice==2 or choice==3):
        choice = int(input(question))
    return choice

x = getChoice('Welcome, '+name+'. Do you dare cross the treacherous sea (1), delve the dangerous dungeon (2), or climb the majestic mountain (3)?')
if x == 1: #sea
    print('You board a ship and set sail, but a storm blows you off course.')
    x = getChoice('Do you curse Neptune (1), stow the sails (2), or drop anchor (3)?')
    if x==1:
        print('The Sea God rises from the depths and smites you with his trident.')
        print('You die.')
    elif x==2:
        print('You wisely stow the sails and weather the storm.')
        print('You find a new trade route. '+name+' is recognized as a bold and capable explorer.')
    else:
        print('Your ship takes on water, the anchor is worse than useless. The ship breaks apart.')
        print('You drown.')
elif x == 2: #dungeon
    print('You enter the dungeon. A tunnel collapse immediately blocks your exit.')
    x = getChoice('Do you dig your way out (1), light a torch (2), or sneak deeper into the catacombs (3)?')
    if x==1:
        print('A safe bet. You dig yourself out and return home.')
        print("You hide under your bed sheets.")
        print("That\'s enough adventuring for this year.")
    elif x==2:
        print('Your torch illuminates a wide and tall cavern full of gold, jewels, and magical artifacts.')
        print('Also goblins. Lots of goblins. They tie you up and feed you to their troll.')
        print("You die.")
    else:
        print('Sneaking deeper into the cave, you avoid nasty goblins and stub your toe on a huge diamond.')
        print('You pocket the diamond, find another way out, and invest your diamond cash in a hot new startup.')
        print('Life is good.')
else: #mountain
    print('You begin to climb. A billy goat immediately challenges you with a riddle.')
    print('Kill me and eat for a day. Let me live and eat every day. I can run without a head. What am I?')
    x = getChoice('Misunderstanding, you kill the goat and eat it (1). You give the obvious answer: chicken (2). It is probably a trick, so you guess zebra (3).')
    if x==1:
        print("You eat a goat. It's not very tasty. Your stomach feels bad.")
        print("You decide to climb the mountain some other day, but you never get around to it.")
    elif x==2:
        print('Yes, says the goat. Chicken is correct. You may pass.')
        print("You climb the mountain and see a beautiful view. That's nice.")
    else:
        print('"Zebra? Are you some kind of idiot?" asks the goat.')
        print('The goat transforms into a wizard. He then turns you into a newt.')
        print('You live the rest of your life as a newt. You learn to enjoy eating bugs.')