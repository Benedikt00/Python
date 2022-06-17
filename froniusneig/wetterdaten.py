from bs4 import BeautifulSoup
import requests
def get_weather_data():
    try:
        html = requests.get("https://wetterheute.at/steiermark/wetter-neumarkt-in-steiermark-heute")
        soup = BeautifulSoup(html.text, 'html.parser')
        var = soup.find("div", {"class": "weather"}).text
        wolkig = "Wolkig"
        wolkenlos = "Wolkenlos"
        bewoelkt = "Bewölkt"
        stbewoelkt = "Stark bewölkt"
        heiter = "Heiter"
        regen = "Regen"

        tonum = None

        if var == heiter:
            tonum = 5
        elif var == wolkenlos:
            tonum = 1
        elif var == wolkig:
            tonum = 2
        elif var == bewoelkt:
            tonum = 3
        elif var == stbewoelkt:
            tonum = 4
        elif var == regen:
            tonum = 5

        else:
            print(str(var) + " add this to se code")
            tonum = 0
        return tonum

    except Exception as e:
        print(e)
        return 0

print(get_weather_data())

