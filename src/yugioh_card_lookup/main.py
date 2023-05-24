import json, requests
from dataclasses import asdict, dataclass
from pprint import pprint
from .BigWebPriceFinder import BigWebPriceFinder
from .YuyuteiPriceFinder import YuyuteiPriceFinder
from fuzzywuzzy import process
from .ultimate_requests.name_to_id_dataset import name_to_id_dataset, id_to_name_dataset
from .NameConverter import NAME_CONVERTER

def fuzzy_search(en_name, threshold=80, limit=3):
    matches = process.extract(en_name, name_to_id_dataset.keys(), limit=limit)
    lower_matches = [match[0].lower() for match in matches]
    if en_name.lower() in lower_matches: # exact match
        return [en_name]
    # fuzzy match
    match_names = [match[0] for match in matches if match[1] >= threshold]
    return match_names if len(match_names) > 0 else None


bigweb = BigWebPriceFinder()
yuyutei = YuyuteiPriceFinder()

@dataclass
class CARD:
    id: str
    price: float
    rarity: str
    image_url: str
class CardLookup:
    def __init__(self):
        self.cards = None
        self.ygoprodeck_card_info_endpoint = "https://db.ygoprodeck.com/api/v7/cardinfo.php?name="
        self.card_img_urls = {}
        
    def execute_fuzzy_search(self, user_input):
        self.cards = fuzzy_search(user_input)
        return (not self.cards is None)
    
    def get_card(self):
        return self.cards

    def execute_search_by_id(self, id):
        data = json.loads(id_to_name_dataset)
        result = list(filter(lambda x: x["id"] == id, data["data"]))
        name = result[0]["name"]
        return name
  
    def execute_price_lookup_for_one_card(self, card_name):
        card_converter = NAME_CONVERTER(card_name)
        jp_name = card_converter.get_jp_name()
        prices = bigweb.find_prices(jp_name)
        prices = json.loads(prices.toJSON())['cards']
        
        if len(prices) == 0:
            prices = yuyutei.find_prices(jp_name)
            prices = json.loads(prices.toJSON())['cards']
        if len(prices) == 0:
            return None
        final_data = [asdict(CARD(price['id'], price['price'], price['rarity'], price['image_url'])) for price in prices]
        return {
            card_name: final_data
        }
            
    
    def execute_price_lookup_for_all_cards(self):
        final_data = {}
        for card in self.cards:
            card_data = self.execute_price_lookup_for_one_card(card)
            if not card_data is None:
                final_data.update(card_data)
            
        return final_data