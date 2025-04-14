import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c457c06113c5ff737d41b6d1737a32f2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create = {
    "name": "Homyak",
    "photo_id": 1
}

body_change_name = {
    "pokemon_id": "289195",
    "name": "Homyak2",
    "photo_id": 4
}

add_pokeboll = {
    "pokemon_id": "289195"
}

respons_create = requests.post( url = f'{URL}/pokemons', headers = HEADER , json = body_create) 
print (respons_create.text)

change_name = requests.put (url = f'{URL}/pokemons', headers = HEADER, json = body_change_name) 
print (change_name.text)

add_pokeboll = requests.post( url = f'{URL}/trainers/add_pokeball' , headers = HEADER , json = add_pokeboll) 
print (add_pokeboll.text) 