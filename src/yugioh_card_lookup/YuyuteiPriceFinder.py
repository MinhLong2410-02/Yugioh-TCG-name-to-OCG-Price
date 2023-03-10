# from .PriceFinder import *
from .PriceFinder import *


class YuyuteiPriceFinder(PriceFinder):
    def __init__(self):
        super().__init__()
        self.yuyutei_endpoint = "https://yuyu-tei.jp/game_ygo/sell/sell_price.php"
        self.source = "Yuyu-tei"
        self.yuyutei_icon = "https://yuyu-tei.jp/img/ogp.jpg"
    
        
    
    def find_prices(self, jp_name: str):
        
        url = self.yuyutei_endpoint + "?name=" + urllib.parse.quote(self.format_japanese_name(jp_name))
        
        card_info = CardInfo(url)
        # page = requests.get(url)
        page = urllib3.PoolManager().request('GET', url, headers={'User-Agent': 'Mozilla/5.0'})
        
        soup = BeautifulSoup(page.data, "html.parser")
        divs = soup.find_all("div", {"class": re.compile(r'^group_box.*$')})
        for div in divs:
            raw_rarity = div.find("em", {"class": "gr_color"})
            rarity = self.format_rarity(raw_rarity.text)
            cards = div.find_all("li", {"class": re.compile(r'^card_unit rarity_.*$')})

            for card in cards:
                card_img = card.find("p", {"class": "image"})
                raw_card_id = card.find("p", {"class": "id"})
                raw_price = card.find("p", {"class": "price"})
                raw_image = card.find("p", {"class": "image"})
                card_id = raw_card_id.text.strip()
                price = self.format_price(raw_price.text)
                card_img = raw_image.img["src"].split()[0]
                card = Card(card_id, jp_name, rarity, "Play", price, card_img)
                card_info.add_card(card)

                self.logger = ("YuyuteiPriceFinder.find_prices", "name: {0} rarity: {1} condition {2} price: {3}".format(
                        jp_name,
                        rarity,
                        "Play",
                        price
                    ))

        return card_info

