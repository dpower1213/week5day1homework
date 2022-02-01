from flask import Flask, render_template, request
import requests
app = Flask(__name__)

@app.route('/')
def index():
    
    return render_template('index.html.j2')

@app.route('/pokemon', methods = ['GET', 'POST'])
def pokemon():
    if request.method == 'POST':
        #contact the api and get the info for the pokemon from the form
        name = request.form.get('pokemon')
        url = f"https://pokeapi.co/api/v2/pokemon/{name}"
        response = requests.get(url)
        if response.ok:
            data = response.json()
            if len(data)<=0:
                print('here')
                error_string = f"There is no info for {name}"
                return render_template('pokemon.html.j2', error = error_string)
            
            poke_dict = {
                'name':data['forms'][0]['name'],
                'order':data['order'],
                'ability':data['abilities'][0]['ability']['name'],
                'base_experience':data['base_experience'],
                'front_shiny':data['sprites']['front_shiny'],
                'stat_name1':data['stats'][0]['stat']['name'],
                'stat_rating1':data['stats'][0]['base_stat'],
                'stat_name2':data['stats'][1]['stat']['name'],
                'stat_rating2':data['stats'][1]['base_stat'],
                'stat_name3':data['stats'][2]['stat']['name'],
                'stat_rating3':data['stats'][2]['base_stat']
        
            }
            return render_template('pokemon.html.j2', poke = poke_dict)
        else:
            error_string = "pokemon always causin trouble"
            return render_template('pokemon.html.j2', error = error_string)
    return render_template('pokemon.html.j2')