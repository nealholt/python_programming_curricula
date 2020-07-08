'''
Goal: demonstrate lists, random, and objects.
Three slot machines with different chances of
winning. Rather than slot1, slot2, slot3. Create
and use random to interact with the list. You
have 10 pulls of the slots then you have to guess
which one has the highest average payoff. Then
follow up with a version in which the user enters
the number of slot machines AND the number of
tries the player gets. Then follow up the video
with a version in which the slot machines are
objects instead of min and max values in a list.
'''
import random

#Encapsulation
class SlotMachine:
    def __init__(self, minimum, maximum):
        self.min = minimum
        self.max = maximum
    def getPayout(self):
        return random.randint(self.min,self.max)
    def getAveragePayoff(self):
        return (self.min+self.max)/2

user = int(input("How many machine?"))

slots = []
for i in range(user):
    minimum = random.randint(1,20)
    maximum = random.randint(5,30)
    if minimum > maximum:
        temp = minimum
        minimum = maximum
        maximum = temp
    slots.append(SlotMachine(minimum,maximum))

guesses_count = int(input("How many guesses?"))

for i in range(guesses_count):
    user = int(input("Pull machine 1 -"+str(len(slots))+"?"))
    index = user-1
    payout = slots[index].getPayout()
    print('Your payout was ',payout)

#Determine which slot machine is actually the best
best_index = 0
best_payoff = 0
for i in range(len(slots)):
    avg_payoff = slots[i].getAveragePayoff()
    if avg_payoff > best_payoff:
        best_payoff = avg_payoff
        best_index = i

user = int(input('Which machine is best? 1 -'+str(len(slots))+'?'))
if user == best_index:
    print('Yes, you have the best odds with this machine!')
else:
    print('No')
