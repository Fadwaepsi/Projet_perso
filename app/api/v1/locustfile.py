from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Temps d'attente aléatoire entre les tâches

    @task
    def get_sunrise_sunset(self):
        city = "Paris"  # Ville pour laquelle nous testons
        self.client.post("/", data={"city": city})  # Envoie une requête POST à l'endpoint racine de l'application Flask

class MoonPhaseUser(HttpUser):
    wait_time = between(1, 5)  # Temps d'attente aléatoire entre les tâches

    @task
    def get_moon_phase(self):
        city = "Paris"  # Ville pour laquelle nous testons
        self.client.post("/", data={"city": city})  # Envoie une requête POST à l'endpoint racine de l'application Flask

