import requests

'''Случайная генерация Имени и Фото покемона'''
data_pokemons = {
    "name": "generate",
    "photo": "generate"
}

'''Токен JSON'''
trainer_token_json = {"trainer_token": "ff8b4cfcdf8391186133cc404e6e2d3a"}

'''Данные для регистрации'''
data_reg = {
    "trainer_token": "ff8b4cfcdf8391186133cc404e6e2d3a",
    "email": "ind-evgenij-dudnikov@qa.studio",
    "password": "aHMKa0ciwsiz9vEzUo2V"
}

def reg_trainer():
    url_reg_trainer = 'https://pokemonbattle.me:9104/trainers/reg'
    reg_response = requests.post(url=url_reg_trainer, json=data_reg)

def activ_trainer():
    url_activ_trainer = 'https://pokemonbattle.me:9104/trainers/confirm_email'
    activ_response = requests.post(url=url_activ_trainer, json=trainer_token_json)

def reg_pokemons():
    url_reg_pokemons = 'https://pokemonbattle.me:9104/pokemons'
    reg_response = requests.post(url=url_reg_pokemons, json=data_pokemons, headers=trainer_token_json)
    id_reg = reg_response.json()['id']

def put_pokemons():
    url_put_pokemons = 'https://pokemonbattle.me:9104/pokemons'
    body_for_put = {
    "pokemon_id": "id {id_reg}",
    "name": "generate",
    "photo": "generate"
}
    put_response = requests.put(url=url_put_pokemons,json=body_for_put, headers=trainer_token_json)

def add_pokeball():
    url_add_pokeball = 'https://pokemonbattle.me:9104/trainers/add_pokeball'
    pokemon_id = {"pokemon_id": "id {id_reg}"}
    pokeball_response = requests.post(url=url_add_pokeball, json=pokemon_id, headers=trainer_token_json)

print(reg_trainer(), activ_trainer(), reg_pokemons(), put_pokemons(), add_pokeball(), sep=" ")