import json
import os
import glob
import matplotlib.pyplot as mpl

def plot_data_day(path_to_day):
    power_list = []
    time_list = []
    for filename in glob.glob(os.path.join(path_to_day, '*.json')):  # only process .JSON files in folder.
        if not "average.json" in filename:
            with open(filename, encoding='utf-8', mode='r') as currentFile:
                data = currentFile.read().replace('\n', '')
                # print(data)
                """
                keyword = json.loads(data)["keytolookup"]
                if keyword not in keywordList:
                    keywordList.append(keyword)"""

                print(filename)
                p = json.loads(data)["Body"]["Inverters"]["1"]["P"]
                hour = json.loads(data)["date"]["hour"]
                minute = json.loads(data)["date"]["minute"]
                hour_dez = int(hour) + (int(minute)/60)
                power_list.append(p)
                time_list.append(hour_dez)


    mpl.plot(time_list, power_list)

    mpl.xlim([6, 22])
    mpl.show()


def plot_data_month(path_to_month):
    power_list = []
    time_list = []
    for folder in os.scandir(path_to_month):  # only process .JSON files in folder.
        for filename in glob.glob(os.path.join(folder.path, '*.json')):
            if not "average.json" in filename:
                with open(filename, encoding='utf-8', mode='r') as currentFile:
                    data = currentFile.read().replace('\n', '')

                    print(filename)
                    p = json.loads(data)["Body"]["Inverters"]["1"]["P"]
                    day = json.loads(data)["date"]["day"]
                    hour = json.loads(data)["date"]["hour"]

                    hour_dez = int(day) + (int(hour)/24)
                    power_list.append(p)
                    time_list.append(hour_dez)



#plot_data_day(r"C:\Users\bsimb\Documents\Programmieren_Privat\Python\json-to-ordnerstruct\test\2022\07\03")
plot_data_month(r"C:\Users\bsimb\Documents\Programmieren_Privat\Python\json-to-ordnerstruct\test\2022\07")












