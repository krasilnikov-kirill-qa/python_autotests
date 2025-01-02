import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '513681a3513681a3e6164fdf4e269f330b9ccc07'
TRAINER_ID = 14076
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

@pytest.mark.parametrize('key, value', [('trainer_name', 'MrPower')])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value

def test_part_of_respons():
    response_get = requests.get(url = f'{URL}/trainers', params= {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'MrPower'

'''@pytest.mark.parametrize('key, value', [('trainer_id', TRAINER_ID), ('in_pokeball', '0'), ('status', 1)])
def test_parametrize(key, value):
    response_parametrize = requests.get(url = f'{URL}/pokemons', params= {'trainer_id' : TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value
'''