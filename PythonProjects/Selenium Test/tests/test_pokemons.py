import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '06e377f5174bdfab3be8a74d274f2162'
HEADER = {'Content-Type': 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '29110'
TRAINER_NAME = 'Michael'

def test_status_code():
    response = requests.get(f'{URL}/trainers', params={'trainer_id': TRAINER_ID}, headers=HEADER)
    assert response.status_code == 200

def test_trainer_name_in_response():
    response = requests.get(f'{URL}/trainers', params={'trainer_id': TRAINER_ID}, headers=HEADER)
    assert response.status_code == 200


