from dataclasses import dataclass
import json
@dataclass
class Card:
    id: str
    jp_name: str
    rarity: str
    condition: str
    price: str
    image_url: str

class CardInfo:
    def __init__(self, url):
        self.cards = []
        self.url = url

    def add_card(self, card):
        self.cards.append(card)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)