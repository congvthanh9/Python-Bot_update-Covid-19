import time
import requests
import json
from win10toast import ToastNotifier

def bot_update():
    r=requests.get('https://coronavirus-19-api.herokuapp.com/all')
    data=r.json()
    text=f"Cases:{data['cases']}\nDeaths:{data['deaths']}\nRecovered:{data['recovered']}"

    while True:
        t=ToastNotifier()
        t.show_toast("Covid Update", text, duration=30)


bot_update()