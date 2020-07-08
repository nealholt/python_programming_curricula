'''
Object-oriented Zork as objects review moderately early
in CS2. They did object DnD at the end of the previous
year and really liked it. This is a great intro to objects.
Do everything through input. Have an inventory so they can
practice list operations.

I've got a rough draft below. There's already roughness.
The environment description should change in response to
taking the key.
There needs to be a list of available actions somewhere.
You set up the objects to respond to an inspect command,
but you never wrote the inspect command.
'''
class Location:
    def __init__(self, text):
        #Display this when player enters this location
        #or looks around
        self.text = text
        #A list of objects at this location that the player
        #can interact with.
        self.objects = []

class Object:
    def __init__(self, name, description, keyword,
                location, required_item):
        self.name = name
        self.description = description
        self.keyword = keyword
        self.location = location
        self.required_item = required_item

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []


kitchen = Location("You are in a room with a linoleum floor. There is a refridgerator, sink, and a door to the north.")
living_room = Location("You are in a room with a carpeted floor. There is a fire place in the corner with a key on top, and a door to the south.")

key = Object('key', 'A metal key', 'get', None, None)
kitchen_door = Object('door', 'A simple wooden door', 'open', kitchen, key)
living_room_door = Object('door', 'A simple wooden door', 'open', living_room, None)

kitchen.objects.append(living_room_door)
living_room.objects.append(kitchen_door)
living_room.objects.append(key)

p = Player('Buddy', living_room)

response = input('Play the game? Anything to continue. "quit" to quit')
while response != 'quit':
    response = input(p.location.text+"\nWhat do you do?")
    for o in p.location.objects:
        if o.name in response and o.keyword in response:
            if o.keyword == 'get':
                p.location.objects.remove(o)
                p.inventory.append(o)
                input('You got a '+o.name)
            elif o.keyword == 'open':
                if o.required_item == None or o.required_item in p.inventory:
                    p.location = o.location
                    input('You go through the '+o.name)
