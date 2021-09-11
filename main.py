import requests
import json
import pandas

BASE_URL = "https://api.wheretheiss.at/v1"


class ISS:
    def __init__(self):
        self.url = BASE_URL

    def satellites(self):
        resp = requests.get(f"{self.url}/satellites")

        if resp.status_code == 200:
            print(resp.json())

    def satellite_id(self, value):
        resp = requests.get(f"{self.url}/satellites/{value}")

        if resp.status_code == 200:
            print(resp.json())

    def satellite_positions(self, value):
        resp = requests.get(f"{self.url}/satellites/{value}/positions")

        if resp.status_code == 200:
            print(resp.json())

    def satellite_tles(self, value):
        resp = requests.get(f"{self.url}/satellites/{value}/tles")

        if resp.status_code == 200:
            print(resp.json())

    def coordinates(self, lat, lon):
        resp = requests.get(f"{self.url}/coordinates/{lat},{lon}")

        if resp.status_code == 200:
            print(resp.json())


if __name__ == "__main__":
    iss = ISS()
    loc = iss.satellites()
