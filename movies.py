#importeren van libs
from requests.api import head
from requests.models import Response
from tmdbv3api import TMDb, tmdb, Movie
import urllib3
import requests

#errors uitzetten
urllib3.disable_warnings()

#variabelen instellen
API_key = 'YOUR_API_KEY'
Bearer = 'BEARER_ACCESS_TOKEN'
tmdb = TMDb()
movie = Movie()
tmdb.api_key = API_key
tmdb.language = 'en'

#responsecode valideren
url = "https://api.themoviedb.org/3"
header = {
    'Authorization' : 'Bearer {}'.format(Bearer),
    'Content-Type' : 'application/json;charset=utf-8'
}

Response = requests.request("GET", url, headers=header)
#check status code en programma uitvoeren
if Response.status_code == 204:
    print("U bent verbonden met uw API op The Movie Database.")
    print()
       
    #input vragen
    film = input("Over welke film zoekt u meer informatie? ")
    m = movie.search(film)

    #Resultaat weergeven
    for i in m:
        print("{",i.id,"}")
        print("Title:\n", i.title)
        print("Overview:\n", i.overview)
        print()
    
elif Response.status_code == 404:
    print("De URL is niet gevonden")
else:
    print("Kan niet verbinden met uw API.")
    


