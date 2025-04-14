import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c457c06113c5ff737d41b6d1737a32f2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '32141'

    # Проверяем, что пришёл верный код ответа
def test_trainer_code():
    response_get2 = requests.get (url = f'{URL}/trainers' , params = {'trainer_id' : TRAINER_ID})
    assert response_get2.status_code == 200 

# Проверяем, что пришло верное имя моего тренера
def test_trainer_id():
    response_get = requests.get (url = f'{URL}/trainers' , params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]['trainer_name'] == 'Homyak99'