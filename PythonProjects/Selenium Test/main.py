import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '06e377f5174bdfab3be8a74d274f2162'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' :TOKEN}

body_registration = {
    "trainer_token": TOKEN,
    "email": "Anton-Samara.777@yandex.ru",
    "password": "Iloveqa1"
}
body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}
body_change_name = {
    "pokemon_id": "298013",
    "name": "wartortle",
    "photo_id": 1
}
body_add_pokeball = {
    "pokemon_id": "298013"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)
'''
'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)'''

'''response_change_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change_name)
print(response_change_name.text)'''

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)

