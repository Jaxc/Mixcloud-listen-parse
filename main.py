import urllib.request
import json

with urllib.request.urlopen("https://api.mixcloud.com/Jaxcie/cloudcasts/?limit=100") as url:
    with open('out.txt', "w") as file:

        raw_data = json.loads(url.read().decode())
        reg_listens = ""
        bonus_listen = ""
        for data in reversed(raw_data["data"]) :
            if "bonus" in data["key"] :
                bonus_listen = bonus_listen + '\t' + str(data["play_count"])
            elif "random" in data["key"] :
                other = 0
            else :
                reg_listens = reg_listens + '\t' + str(data["play_count"])

        file.write(reg_listens + '\n\n' + bonus_listen)
