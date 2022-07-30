from flask import render_template, request, redirect, url_for
from .forms import PokeCreationForm
from app.models import Poke
from app import app
from app.models import db
import requests



@app.route('/pokemon', methods=["POST"])
def pokemonCard():
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
                    'type' : data['types'][0]['type']['name'],
                    'ability' : data['abilities'][1]['ability']['name'],
                    'base_experience' : data['base_experience'],
                    'image' : data['sprites']['front_shiny'],
                    'hp' : data['stats'][0]['base_stat'],
                    'attack' : data['stats'][1]['base_stat'],
                    'defense' : data['stats'][2]['base_stat'],
                }
                print(pokemon_dict)
                return render_template('pokemon.html', pokemon_dict = pokemon_dict, pokemon = pokemon, form = form)
    else:
        print('invalid')


    return render_template('pokemon.html', form = form)


@app.route('/', methods=["GET","POST"])
def index():
    form = PokeCreationForm()
    if request.method == 'POST':
        print('POST request made')
        if form.validate():
            poke_name = form.poke_name.data

            print(poke_name)

            # add pokemon to database
            poke = Poke(poke_name)

            #add instance to our db(database)
            db.session.add(poke)
            db.session.commit()

            return redirect(url_for('app.pokemonCard'))
        else:
            print("validation failed")
    else:
        print('GET request made')
    return render_template('index.html', form = form)


@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name = user))

    return render_template(login.html)