import random

class Room:
    def __init__(self, name, probability, is_dirty=True):
        self.name = name
        self.is_dirty = is_dirty
        self._probability = probability
        self.random_generator = random.SystemRandom()

    def clean(self):
        self.is_dirty = False

    def make_dirty(self):
        if not self.is_dirty:
            random_value = self.random_generator.random()
            
            if random_value < self._probability:
                self.is_dirty = True
        
    def return_state(self):
        if self.is_dirty:
            return "D"
        
        return "C"

    def is_room_dirty(self):
        return self.is_dirty


