
from datetime import date
from os import makedirs
from pathlib import Path
from random import randint

from httpx import get, stream
from rocketry import Rocketry
from rocketry.args import Arg, Return
from rocketry.conds import after_success

POKE_API = 'https://pokeapi.co/api/v2/pokemon'
DOLAR_API = 'https://economia.awesomeapi.com.br/json/daily/USD-BRL/?start_date={}&end_date={}'


app = Rocketry()

@app.param('date')
def random_date_generator():
    day = randint(1,28)
    month = randint(1,12)
    year = randint(2015,2022)

    random_date = date.today().replace(
        day=day,month=month,year=year
    )

    formated_date = random_date.strftime('%Y%m%d')

    return formated_date

@app.task('every 2s', name='Pega cotação dólar')
def get_dolar(date=Arg('date')):
    response = get(DOLAR_API.format(date, date)).json()[0]['high']
    return response.replace(".","")[:3]

@app.task(after_success(get_dolar))
def get_pokemon_json(number=Return(get_dolar)):
    response = get(f'{POKE_API}/{number}').json()
    return response

@app.task(after_success(get_pokemon_json))
def get_pokemon_sprite_url(poke_json=Return(get_pokemon_json)):
    return(
        poke_json['sprites']['front_default'],
        poke_json['name']
    )
@app.task(after_success(get_pokemon_sprite_url))
def download_sprite(
    poke_data = Return(get_pokemon_sprite_url),
    poke_number = Return(get_dolar)
    ):
    url, name = poke_data
    path = Path(f"{poke_number}_{name}.png")
    with open(path,"wb") as download_file:
        with stream("GET", url) as s:
            for chunck in s.iter_bytes():
                download_file.write(chunck)
    return path

@app.task(after_success(download_sprite))
def move_sprite(path: Path = Return(download_sprite)):
    makedirs("sprites", exist_ok=True)
    pasta = Path('sprites')
    path.rename(pasta / path)

app.run()