
class Location:
    def __init__(self, description):
        self.description = description
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.pickups = []

    def addPickup(self, x):
        self.pickups.append(x)

    def removePickup(self, x):
        self.pickups.remove(x)
        return x

dining_room = Location('a fancy dining room.')

kitchen = Location('a messy kitchen with flour on the counter and dishes in the sink.')
kitchen.addPickup('flour')
kitchen.addPickup('dishes')

bath = Location('a small bathroom with a towel on the floor.')
bath.addPickup('towel')
porch = Location('a wooden porch with a rocking chair.')
bedroom = Location('a bedroom with a watch on the bedside table')
bedroom.addPickup('watch')

dining_room.north = kitchen
dining_room.east = bedroom
dining_room.west = bath
dining_room.south = porch

kitchen.south = dining_room

location = dining_room

response = ''
while response != 'quit':
    response = input('You see '+location.description)
    if response == 'north':
        location = location.north
    elif response == 'south':
        location = location.south
    elif response == 'east':
        location = location.east
    elif response == 'west':
        location = location.west
    elif response.startswith('take '):
        success = False
        for pickup in location.pickups:
            if response.endswith(pickup):
                location.removePickup(pickup)
                success = True
                break
        if success:
            print('Picked up '+pickup)
        else:
            print('Command not recognized.')

print('Finished')
