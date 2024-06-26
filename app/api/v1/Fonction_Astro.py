from flask import Flask, render_template, request
import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('api_key')

app = Flask(__name__)

def sauvegarder_heures_soleil(data, nom_fichier):
    """
    Sauvegarde les heures de lever et de coucher du soleil dans un fichier JSON.

    Args:
        data (dict): Les données à sauvegarder.
        nom_fichier (str): Le nom du fichier JSON de sortie.
    """
    chemin_dossier = "data"
    chemin_fichier = os.path.join(chemin_dossier, nom_fichier)
    
    if not os.path.exists(chemin_dossier):
        os.makedirs(chemin_dossier)
    
    with open(chemin_fichier, "w") as json_file:
        json.dump(data, json_file, indent=4)

def get_sunrise_sunset(city, api_key):
    url = f"http://api.weatherapi.com/v1/astronomy.json?key={api_key}&q={city}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        astronomy_data = data.get("astronomy", {})
        
        if astronomy_data:
            sunrise = astronomy_data["astro"]["sunrise"]
            sunset = astronomy_data["astro"]["sunset"]
            sauvegarder_heures_soleil({"sunrise": sunrise, "sunset": sunset}, "sunrise_sunset.json")
            return sunrise, sunset
    else:
        print(f"Erreur lors de la récupération des données astronomiques: {response.status_code}")
    
    return None, None

@app.route('/', methods=['GET', 'POST'])
def index():
    sunrise = None
    sunset = None
    city = None
    
    if request.method == 'POST':
        city = request.form['city']
        try:
            sunrise, sunset = get_sunrise_sunset(city, api_key)
            if not sunrise or not sunset:
                raise Exception('Erreur lors de la récupération des heures de soleil')
        except Exception as e:
            sunrise = sunset = str(e)
    
    return render_template('index.html', sunrise=sunrise, sunset=sunset, city=city)

if __name__ == '__main__':
    app.run(debug=True)
