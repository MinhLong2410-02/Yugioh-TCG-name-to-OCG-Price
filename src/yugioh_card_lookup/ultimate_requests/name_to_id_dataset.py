import requests
name_to_id_dataset = requests.get("https://db.ygorganization.com/data/idx/card/name/en").json()