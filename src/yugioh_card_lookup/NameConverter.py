from .ultimate_requests.name_to_id_dataset import name_to_id_dataset
import requests

class NAME_CONVERTER:
    
    def __init__(self, en_name: str):
        self.en_name = en_name
        self.card_name_head_url = "https://db.ygorganization.com/data/card/"
        try:
            self.id = name_to_id_dataset[self.en_name][0]
        except KeyError:
            self.id = None
            
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.en_name
        
    def get_jp_name(self):
        url = self.card_name_head_url + str(self.id)
        data = requests.get(self.card_name_head_url + str(self.id)).json()
        return data['cardData']['ja']['name']
            