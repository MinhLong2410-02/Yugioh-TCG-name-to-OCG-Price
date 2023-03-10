from .PriceFinder import *

class BigWebPriceFinder(PriceFinder):
    def __init__(self):
        super().__init__()
        self.bigweb_endpoint = "https://bigweb.co.jp/ver2/yugioh_index.php"
        self.bigweb_api_endpoint = "https://api.bigweb.co.jp/products"
        
        
    def find_prices(self, en_name: str):
        
        jp_name = self.format_name_for_search_engine(en_name)
        
        
        url = self.bigweb_endpoint \
            + "?search=yes&type_id=9&action=search&shape=1&seriesselect=&tyselect=&colourselect=&langselect=&condiselect=&selecttext=" \
            +  urllib.parse.quote(self.format_japanese_name(jp_name))
        card_info = CardInfo(url)
        params = {
            'game_id': 9,
            'name': self.format_japanese_name(jp_name),
        }   
        
        r = requests.get(self.bigweb_api_endpoint, params=params)
        
        raw_card_infos = r.json()['items']
        
        for raw_card_info in raw_card_infos:
            
            card_id = raw_card_info["fname"]
            raw_rarity = raw_card_info["rarity"]["slip"]
            rarity = self.format_rarity(raw_rarity)
            raw_condition = raw_card_info["condition"]
            raw_condition = raw_condition["slip"] if raw_condition else "None"
            condition = "Scratch" if raw_condition == "キズ" else "Play"
            price = raw_card_info["price"]
            image_url = raw_card_info["image"]
            self.logger = "BigWebPriceFinder.find_prices", "name: {0} rarity: {1} condition {2} price: {3}".format(
                jp_name,
                rarity,
                condition,
                price
            )
            card = Card(card_id, jp_name, rarity, condition, price, image_url)
            card_info.add_card(card)

        return card_info
