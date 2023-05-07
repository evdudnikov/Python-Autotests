import pytest
import requests

def test_status_code():
    url = 'https://pokemonbattle.me:9104/trainers'
    response = requests.get(url)
    response_trainer_id = requests.get(url=url, params={'trainer_id':'4297'})
    assert response.status_code == 200
    assert response_trainer_id.status_code == 200