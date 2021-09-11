import urllib.request
import json
import webbrowser

ISS_URL = 'http://api.open-notify.org/iss-now.json'
MAP_URL = 'https://www.openstreetmap.org'


class LoadPosition:
    def __init__(self):
        self.iss_url = ISS_URL
        self.map_url = MAP_URL

    def getlatlong(self):
        response = urllib.request.urlopen(self.iss_url)
        print(response)
        obj = json.loads(response.read())
        lat = obj['iss_position']['latitude']
        long = obj['iss_position']['longitude']

        return lat, long

    def openurl(self):
        '''
        example map url
        https://www.openstreetmap.org/?mlat=38.9212&mlon=-80.8151#map=3/38.92/-80.82
        '''

        lat, long = self.getlatlong()
        url = f"{self.map_url}/?mlat={str(lat)}&mlon={str(long)}#map=3/{str(lat)}/{str(long)}"
        webbrowser.open_new_tab(url)


if __name__ == "__main__":
    load = LoadPosition()
    load.openurl()
