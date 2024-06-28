from api.v1.Fonction_Astro import get_sunrise_sunset, get_moon_phases
from fastapi import FastAPI, HTTPException

app = FastAPI()

api_key = "4c57c92aa17e4b82857172100241506"

@app.get("/heures/{city}")
def read_sunrise_sunset(city: str):
    try:
        sunrise, sunset = get_sunrise_sunset(city, api_key)
        if sunrise and sunset:
            return {f"L'heure de lever et coucher de soleil à": city, "est": sunrise, "et": sunset}
        else:
            raise HTTPException(status_code=404, detail="Data not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/phases_lune/{city}")
def read_moon_phases(city: str):
    try:
        moon_phase = get_moon_phases(city, api_key)
        if moon_phase:
            return {f"La phase de la lune à": city, "est": moon_phase}
        else:
            raise HTTPException(status_code=404, detail="Data not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
