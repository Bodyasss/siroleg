class Card:
    def __init__(self, name: str, description: str = ""):
        self.name = name
        self.description = description

    def __str__(self):
        return self.name


class Item(Card):
    def __init__(
        self,
        name: str,
        bonus: int,
        slot: str,
        hands_required: int = 0,
        description: str = "",
        usable_by: list[str] = None,
    ):
        super().__init__(name, description)
        self.bonus = bonus
        self.slot = slot
        self.hands_required = hands_required  
        self.usable_by = usable_by if usable_by else []

    def is_usable_by(self, player_class: str, player_race: str) -> bool:
        if not self.usable_by:
            return True  
        return player_class in self.usable_by or player_race in self.usable_by
