class VacuumCleaner:
    def __init__(self, initial_position, dirt_locations):
        self.position = initial_position
        self.dirt_locations = set(dirt_locations)
        self.cleaned_locations = set()

    def is_dirty(self):
        return self.position in self.dirt_locations

    def suck_dirt(self):
        if self.is_dirty():
            print(f"Sucking dirt at position {self.position}")
            self.dirt_locations.remove(self.position)
            self.cleaned_locations.add(self.position)
        else:
            print(f"No dirt at position {self.position}")

    def move_left(self):
        print("Moving left")
        self.position -= 1
        self.position = max(self.position, 0)

    def move_right(self, room_size):
        print("Moving right")
        self.position += 1
        self.position = min(self.position, room_size - 1)

    def clean_room(self, room_size):
        print(f"Initial state: {self.position}, Dirt locations: {self.dirt_locations}")

        while self.dirt_locations:
            self.suck_dirt()

            if self.position % 2 == 0:  # Move right on even positions
                self.move_right(room_size)
            else:  # Move left on odd positions
                self.move_left()

            print(f"Current state: {self.position}, Dirt locations: {self.dirt_locations}")

        print(f"Room cleaned. Cleaned locations: {self.cleaned_locations}")

if __name__ == "__main__":
    room_size = 5
    initial_position = 0
    dirt_locations = [1, 3, 4]

    vacuum_cleaner = VacuumCleaner(initial_position, dirt_locations)
    vacuum_cleaner.clean_room(room_size)
