import random
from abc import ABC,abstractmethod

class Player(ABC):
    def __init__(self):
        self.moves = []
        self.position = (0, 0)
        self.path = [self.position]
    
    def make_move(self):
        """Select a random move, update position, append to path, return new position"""
        move = random.choice(self.moves)
        self.position = (self.position[0] + move[0], self.position[1] + move[1])
        self.path.append(self.position)
        return self.position
    
    @abstractmethod
    def level_up(self):
        """Abstract method to be implemented by concrete classes"""
        pass

class Pawn(Player):
    def __init__(self):
        super().__init__()
        self.moves=[(0,1),(0,-1),(-1,0),(1,0)]

    def level_up(self):
        diagonal_moves=[(-1,1),(1,1),(-1,-1),(1,-1)]
        self.moves.extend(diagonal_moves)
