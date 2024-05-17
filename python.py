class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def add_paths(self, paths):
        self.paths.update(paths)


def play_game(starting_room):
    current_room = starting_room

    while True:
        print("\n" + "-" * 20)
        print("You are in the", current_room.name)
        print(current_room.description)
        print("Available paths:")
        for path in current_room.paths.keys():
            print("-", path)

        choice = input("Choose a path: ").lower()

        if choice in current_room.paths:
            current_room = current_room.paths[choice]
        else:
            print("Invalid choice. Try again.")


# Create rooms
kitchen = Room("Kitchen", "A small, tidy kitchen.")
living_room = Room("Living Room", "A spacious living room with comfortable sofas.")
bedroom = Room("Bedroom", "A cozy bedroom with a large bed.")

# Add paths between rooms
kitchen.add_paths({"living room": living_room})
living_room.add_paths({"kitchen": kitchen, "bedroom": bedroom})
bedroom.add_paths({"living room": living_room})

# Start the game
play_game(kitchen)