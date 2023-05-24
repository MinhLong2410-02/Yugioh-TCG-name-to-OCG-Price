import requests
name_to_id_dataset = requests.get("https://db.ygorganization.com/data/idx/card/name/en").json()
id_to_name_dataset = requests.get("https://db.ygoprodeck.com/api/v7/cardinfo.php").text