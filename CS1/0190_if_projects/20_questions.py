#You get the idea:

answer = input('Is it a physical object?').lower()
if answer == 'yes' or answer == 'y':
    answer = input('Is it alive?').lower()
    if answer == 'yes' or answer == 'y':
        answer = input('Is it an animal?').lower()
        if answer == 'yes' or answer == 'y':
            answer = input('Is it a land animal?').lower()
            if answer == 'yes' or answer == 'y':
                print('Are you thinking of a dandelion?')
            else:
                print('Are you thinking of a Ecoli?')
        else:
            answer = input('Is it a plant?').lower()
            if answer == 'yes' or answer == 'y':
                print('Are you thinking of a dandelion?')
            else:
                print('Are you thinking of a Ecoli?')
else:
    answer = input('Is it an emotion?').lower()
