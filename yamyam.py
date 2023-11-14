import requests

def check(city):
    apikey = '701ddd2366550d5f2fa875a38da1c12a464d8178'

    url = f"https://api.waqi.info/feed/{city}/?token={apikey}"

    respuesta = requests.get(url)

    jason = respuesta.json()

    aqi = jason["data"]['aqi']
    
    return f"La AQI en {city} es {aqi}"
print(check("Santiago"))