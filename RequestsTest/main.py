import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '513681a3e6164fdf4e269f330b9ccc07'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
body_create_pokemon = {
    "name": "generate",
    "photo_id": -1
}

#Создание покемона
response_create_pokemon = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon)
print(response_create_pokemon.json())

id_create_pokemon = response_create_pokemon.json()['id']

#Смена имени покемона
body_change_name_pokemon = {
    "pokemon_id": id_create_pokemon,
    "name": "Минимиш",
    "photo_id": 2
}

response_change_name_pokemon = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name_pokemon)
print(response_change_name_pokemon.json())

#Поймать покемона в покебол
body_add_pokeball = {
    "pokemon_id": id_create_pokemon
}

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.json())





'''Запросы нужно писать друг за другом в **одном** файле
- Создание покемона (**POST /pokemons** (*не забудь про нужный хэдер*))
В ответе (терминале) должен прийти объект json
- Смена имени покемона (**PUT /pokemons** (*не забудь про нужный хэдер*))
В ответе (терминале) должен прийти объект json
- Поймать покемона в покебол (**POST /trainers/add_pokeball** (*не забудь про нужный хэдер*))
В ответе (терминале) должен прийти объект json'''