class VacuumAgent:

    def __init__(self, rooms):
        self.rooms = rooms
        self.status = {room: "Unknown" for room in rooms}

    def action(self, location, condition):

        self.status[location] = condition

        if condition == "Dirty":
            return "Clean"

        if all(x == "Clean" for x in self.status.values()):
            return "Stop"

        if location == "A":
            return "Right"
        else:
            return "Left"


def vacuum():

    rooms = ["A", "B"]

    house = {
        "A": "Dirty",
        "B": "Dirty"
    }

    agent = VacuumAgent(rooms)

    location = "A"

    while True:

        print("Agent is in room", location)

        condition = house[location]

        move = agent.action(location, condition)

        if move == "Clean":
            house[location] = "Clean"
            print("Room cleaned")

        elif move == "Right":
            location = "B"
            print("Moved to B")

        elif move == "Left":
            location = "A"
            print("Moved to A")

        elif move == "Stop":
            print("All rooms are clean!")
            break


vacuum()
