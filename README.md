# AstroProject

[![forthebadge](http://forthebadge.com/images/badges/built-with-love.svg)](http://forthebadge.com)  [![forthebadge](http://forthebadge.com/images/badges/powered-by-electricity.svg)](http://forthebadge.com)

Cette interface est développé à partir d'une fonctionnalité de l'API météorologique, qui nous affiche l'heure exacte de lever et coucher de soleil d'une ville.

### Pré-requis

Pour commencer il faut :

- Développer la fonctionnalité Astronomique qui se trouve dans le site de l'API https://www.weatherapi.com/.
- Vous avez besoin d'une clé API pour accéder aux services d'une API météo.
- Assurer l'activation de votre environnement.
- Créer un nouveau repositorie.
### Installation

Les étapes pour installer votre programme :
- Installer Fastapi : pip install fastapi
- Installer les requests : pip install requests
- Installer la bibliothèque python-dotenv : pip install python-dotenv
- Installer Flask : pip install flask
- Installer Pytest : pip install pytest 
- Créer l'environnement virtuel : python -m venv env
- Activer l'environnement : .\venv\Scripts\activate
- Installer flake8 : pip install flake8 flake8-html flake8
- générer le rapport HTML : flake8 --format=html --htmldir=flake8-report
- Installer les dépendance : pip install -r requirement.txt

Ensuite vous pouvez montrer ce que vous obtenez au final...

## Démarrage

- Assurer que l'api est bien exécuté.
- lancez le serveur FastAPI : uvicorn app.main:app --reload
- Accédez à l'url affiché en le coppiant dans votre navigateur.
- Exécuter l'application Flask  : python main.py
- Accédez à http://127.0.0.1:5000 dans votre navigateur pour voir l'interface utilisateur web.

## Tests

- Vérifier la qualité du code avec flake8 : pip install flake8
- Exécuter les tests unitaires en utilisant Pytest : pip install pytest ==> python test_Astro.py
- Générer le rapport HTML : flake8 --format=html --htmldir=flake8-report

## Auteurs

Fadwa BAYOUDH


