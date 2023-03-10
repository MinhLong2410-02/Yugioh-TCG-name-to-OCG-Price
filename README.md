# Yugioh Lookup: TCG Name to OCG Price

## Source code is based on Solomon API, github link: [punparin/solomon-api: A REST API to retrieve Yugioh OCG cards' price (github.com)](https://github.com/punparin/solomon-api)

This is an upgraded version since it adds more features:
- Turn English name to its Japanese version
- Perform fuzzy search on card's name

## English to Japanese
Each Yu-gi-oh card is marked with an official Konami ID, this data can be found by making API calls to: **https://db.ygorganization.com/data/idx/card/name/en**

By getting card's ID, Japanese name, Italian Name, Deutsch....can be found by making API calls to: **https://db.ygorganization.com/data/card/{ID}** 


## Fuzzy search
Fuzzy search gives out 3 most accurate card names if its string matching is not 100%

## OCG Price from Big Web API and Yuyutei scraper
Yuyutei scraper, Big Web API is from *Solomon.*

## How to use
>!pip install -r requirements.txt

In Python file:
**from src.yugioh_card_lookup import CardLookup**

### Credits goes to:
- Puparin, check out his github: [punparin (Parin Kobboon) (github.com)](https://github.com/punparin)
- Ygoprodeck: [YGOPRODeck – Download and Share Yu-Gi-Oh! Decks](https://ygoprodeck.com/)
- Ygorganization: [About our API – Card Database (ygorganization.com)](https://db.ygorganization.com/about/api)