
import zroya
import requests
import datetime
import time
import requests
from bs4 import BeautifulSoup as BS
import matplotlib.pyplot as plt
import json

json_file = open("items.json")
items_to_get = json.load(json_file)
json_file.close()

zroya.init("python", "a", "b", "c", "d")

#   "": {
#   "amazon": "",
#   "preis_notification_freshold": 0
#  }

# Template for question
ask_template = zroya.Template(zroya.TemplateType.ImageAndText4)
ask_template.setFirstLine("Es gibt ein neues Angebot")
ask_template.setSecondLine("Der {werkzeug} kostet nur {preis}€".format(werkzeug="", preis=45))
ask_template.setThirdLine("{preis_unter} € unter dem Angegebenen Wert".format(preis_unter=23))
ask_template.setImage("sale.ico")
ask_template.addAction("Link")
ask_template.addAction("Preisvergleich")

# Response for OK
ok_template = zroya.Template(zroya.TemplateType.Text1)
ok_template.setFirstLine("I'm sorry to hear that!")


def onAction(nid, action_id):
    global fine_template, ok_template

    if action_id == 0:
        import webbrowser

        url = amazon_url
        webbrowser.register('opera', None,
                            webbrowser.BackgroundBrowser(
                                "C://Users//bsimb//AppData//Local//Programs//Opera GX//launcher.exe"))
        webbrowser.get('opera').open(url)
    else:

        json_file_for_plotting = open("items.json")
        items_to_get_for_plotting = json.load(json_file_for_plotting)
        json_file_for_plotting.close()

        x = []
        y = []

        for data_for_plotting in items_to_get_for_plotting[key]["datensatz"]:
            x.append(data_for_plotting[0])
            y.append(data_for_plotting[1])

        # plot
        plt.plot(x, y)
        # beautify the x-labels
        plt.gcf().autofmt_xdate()

        plt.show()


while True:

    for key in items_to_get:
        amazon_url = items_to_get[key]["amazon"]

        if amazon_url is not None:
            amazon_page = requests.get(amazon_url, headers={
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/101.0.4951.67 Safari/537.36"})
            amazon_page = BS(amazon_page.content, "html.parser")
            amazon_price = amazon_page.find("span", {"class": "a-offscreen"})
            amazon_price = str(amazon_price)  # <span class="a-offscreen">€54.44</span>
            amazon_price = amazon_price.replace("€", "")
            amazon_price = amazon_price.replace("<span class=\"a-offscreen\">", "")
            amazon_price = amazon_price.replace("</span>", "")
            amazon_price = amazon_price.replace(",", ".")
            amazon_price = float(amazon_price)

            freshold = items_to_get[key]["preis_notification_freshold"]
            if amazon_price <= freshold:
                ask_template.setSecondLine(
                    "Der {werkzeug} kostet nur {preis}€".format(werkzeug=key, preis=amazon_price))
                ask_template.setThirdLine("{preis_unter} € unter dem Schmerzpreis".format(
                    preis_unter=round(abs(amazon_price - freshold), 2)))
                zroya.show(ask_template, on_action=onAction)
                time.sleep(30)

            with open("items.json", "r+") as data_file:
                data = json.loads(data_file.read())
                data[key]["datensatz"].append([datetime.datetime.now(), amazon_price])
                data_file.seek(0)
                data_file.write(json.dumps(data, indent=4, sort_keys=True, default=str))
                data_file.truncate()
                data_file.close()
    print("Loop")
    time.sleep(60*60*4)
