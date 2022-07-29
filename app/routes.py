from flask.globals import request
from flask import render_template, request, redirect, url_for
from .forms import PokeCreationForm

# import models
# from app.models import Poke



from app import app
from flask import render_template

from app.models import db

import requests

import json


@app.route('/pokemon')
def pokemonCard():


    return render_template('pokemon.html')


@app.route('/', methods=["GET","POST"])
def index():
    form = PokeCreationForm()



    if request.method == "POST":
        if form.data:
            print(form.data)

            pokemon = form.data['poke_name'].lower()

            response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}')
            if response.ok:
                data = response.json()

                pokemon_dict = {
                    'name' : data['name'],
                    'ability' : data['abilities'][1]['ability']['name'],
                    'base_experience' : data['base_experience'],
                    'image' : data['sprites']['front_shiny'],
                    'hp' : data['stats'][0]['base_stat'],
                    'attack' : data['stats'][1]['base_stat'],
                    'defense' : data['stats'][2]['base_stat'],
                }
                print(pokemon_dict)
                return render_template('index.html', pokemon_dict = pokemon_dict, pokemon = pokemon, form = form)
    else:
        print('invalid')


    return render_template('index.html', form = form)