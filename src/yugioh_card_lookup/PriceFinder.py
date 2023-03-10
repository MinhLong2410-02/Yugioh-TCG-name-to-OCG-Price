import requests
import re
import json
import urllib.parse
import urllib3
from bs4 import BeautifulSoup
from http import HTTPStatus
from .CardInfo import CardInfo, Card
from .ultimate_requests import name_to_id_dataset
from .NameConverter import NAME_CONVERTER



class PriceFinder:
    def __init__(self):
        self.logger = ""
        self.ygoprodeck_card_info_endpoint = "https://db.ygoprodeck.com/api/v7/cardinfo.php"
        self.fandom_endpoint = "https://yugioh.fandom.com/wiki"
        self.bigweb_endpoint = "https://bigweb.co.jp/ver2/yugioh_index.php"
        self.yuyutei_endpoint = "https://yuyu-tei.jp/game_ygo/sell/sell_price.php"
        self.rarity_alias = self.load_rarity_alias_config()

    def load_rarity_alias_config(self):
        return {
            "ｼｰｸﾚｯﾄ": "SCR",
            "【TRC1】ﾚｱﾘﾃｨ･ｺﾚｸｼｮﾝ": "CR",
            "ｱﾙﾃｨﾒｯﾄ": "UTM",
            "SP": "SR",
            "SPPR": "SPR",
            "Mil-Super": "MSR",
            "KC-Ultra": "KCUR",
            "Ｇ": "GR",
            "P-N": "NP",
            "SE": "SCR",
            "UL": "UTM",
            "HR": "HL",
            "ステンレス": "Stainless"
        }


    def format_japanese_name(self, name):
        name = name.replace("－", " ")
        
        return name

    def format_price(self, price):
        return price.strip().replace("円", "")

    def format_rarity(self, rarity):
        rarity = rarity.strip()
        if rarity in self.rarity_alias:
            return self.rarity_alias[rarity]
        
        return rarity

    def format_name_for_search_engine(self, name):
        return name.replace("－", "−")