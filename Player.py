from typing import List
from cards import Item

class Player:
    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.hand: List[Item] = []
        self.equipment = {
            "headgear": None,
            "armor": None,
            "footgear": None,
            "hands": []
        }
        self.player_class = None
        self.player_race = None
        
    def gain_level(self, amount=1):
        self.level += amount
        self.level = min(self.level, 10)
        print(f"{self.name} достиг уровня {self.level}")
        
    
        
