import json
import os
import glob
import datetime
import shutil
from time import sleep

def move_files(files_path, ordner_path):

    """
    moves files from on folder into the other, creates folder structure
    """


    def get_date(file_path):
        """
        gives back a dict containing jear, month, day, hour and minute from filename like '20220630200950.json'
        """

        filename = os.path.splitext(os.path.basename(file_path)) #(1235312, .json)
        date = filename[0]
        jear = date[0:4]
        month = date[4:6]
        day = date[6:8]
        hour = date[8:10]
        minute = date[10:12]

        date_time = {"jear": jear, "month": month, "day": day, "hour": hour, "minute": minute}
        return date_time

    def path_from_dict(date_dict, goal_folder):
        """
        takes a dict like this
        '{"jear": jear, "month": month, "day": day, "hour": hour, "minute": minute}'
        and a folder
        and returns a path like this
        'C:/User/folder/2022\07\01'
        """
        d = date_dict
        path = "/" + d["jear"] + "/"+ d["month"] + "/" + d["day"]
        path = goal_folder + path
        return path

    for filename in glob.glob(os.path.join(files_path)):
        
        date_dict = get_date(filename)
        with open(filename, encoding='utf-8', mode='r+') as c:
            dc = json.loads(c.read())

            del dc["Body"]["Site"]
            del dc["Head"]["RequestArguments"]
            del dc["Head"]["Status"]
            
            dc.update({"date": date_dict})
            
            c.seek(0)

            c.write(json.dumps(dc))
            c.truncate()

            c.close()

        os.makedirs(path_from_dict(date_dict, ordner_path), exist_ok=True)
        shutil.copy(filename, path_from_dict(date_dict, ordner_path) )
        os.remove(filename)

def Average(lst):
    try:
        return sum(lst) / len(lst)
    except ZeroDivisionError:
        print("Kein Element in der Liste")
        return 0

#def add_zero_if_under_ten(int):
#    if int < 10:
#        return "0" + str(int)
#    else:
#        return str(int)

def check_if_full(path, date="day"):
    """
    checks if there is already a a folder for the next day if not, incomplete
    :param path: check if this folder is full
    :param date: put in a string: day, month or year (default is day)
    :return: True or False
    """


    if date == "day":
        #pfad ohne letzten folder

        day = os.path.basename(os.path.normpath(path))

        month_folder = os.path.dirname(path)
        month = os.path.basename(os.path.normpath(month_folder))

        year_folder = os.path.dirname(month_folder)
        year = os.path.basename(os.path.normpath(year_folder))

        root_path = os.path.dirname(year_folder)

        day_plus_1 = "{:02d}".format(int(day) + 1)
        month_plus_1 = "{:02d}".format(int(month) + 1)
        year_plus_1 = int(year) + 1

        if os.path.exists(str(month_folder + "\\" + day_plus_1)):
            return True
        elif os.path.exists(str(year_folder + "\\" + month_plus_1)):
            return True
        elif os.path.exists(str(root_path) + "\\" + str(year_plus_1)):
            return True
        else:
            return False

    elif date == "month":
        #pfad ohne letzten folder

        month_folder = path
        month = os.path.basename(os.path.normpath(path))

        year_folder = os.path.dirname(path)
        year = os.path.basename(os.path.normpath(month_folder))

        root_path = os.path.dirname(year_folder)

        month_plus_1 = "{:02d}".format(int(month) + 1)
        year_plus_1 = int(year) + 1

        if os.path.exists(str(year_folder + "\\" + month_plus_1)):
            return True
        elif os.path.exists(str(root_path) + "\\" + str(year_plus_1)):
            return True
        else:
            return False

    elif date == "year":
        # pfad ohne letzten folder

        year_folder = path
        year = os.path.basename(path)

        root_path = os.path.dirname(year_folder)

        year_plus_1 = int(year) + 1

        if os.path.exists(str(root_path) + "\\" + str(year_plus_1)):
            return True
        else:
            return False

def add_averages_to_file_system(ordner_path):
    """
    Adds an average.json-file to every full day, month, year
    :param ordner_path: the path to the root of the file system
    :return:
    """
    av_power_d = []

    av_power_m = []

    av_power_y = []
    
    for year in os.scandir(ordner_path):
        if not os.path.exists(str(year.path) + "\\" + "average.json"):                                #|
            for months in os.scandir(year):                                                           #|Loops through the directory system checking if
                if not os.path.exists(str(months.path) + "\\" + "average.json"):                      #| the average-file for the day, month, year already exists
                    for days in os.scandir(months):                                                   #|
                        if not os.path.exists(str(days.path) + "\\" + "average.json"):                #|
                            if check_if_full(days):

                                # finds the average of the day
                                for files in os.scandir(days):
                                    if not "average" in files.path:     #checks if the current file is the average file for safety because then it would not find the power
                                        with open(files, mode='r') as currentFile:

                                            data = currentFile.read().replace('\n', '')
                                            try:
                                                p = json.loads(data)["Body"]["Inverters"]["1"]["P"]
                                            except KeyError as e:
                                                print(e)
                                                print(files.path)
                                            av_power_d.append(p)
                                #saves the average power
                                av_power_d_num = Average(av_power_d)

                                #creates the average file for the day
                                with open(os.path.join(days.path, 'average.json'), 'w') as f:
                                    av = {"average": av_power_d_num}
                                    f.write(json.dumps(av))
                                    f.close()

                    if check_if_full(months, "month"):

                        for days in os.scandir(months):
                            #open the average files in the days
                            for jsons in glob.glob(os.path.join(days, '*.json')):

                                if "average.json" in jsons: #we only want the average.json file to be opened
                                    with open(jsons, 'r') as currentFile:
                                        data = currentFile.read().replace('\n', '')
                                        p = json.loads(data)["average"]
                                        av_power_m.append(p)

                        #calculate average for the month
                        av_power_m_num = Average(av_power_m)

                        # creates the average file for the month
                        with open(os.path.join(months.path, 'average.json'), 'w') as f:
                            av = {"average": av_power_m_num}
                            f.write(json.dumps(av))
                            f.close()

        if check_if_full(year, "years"):
            # open the average files in the months
            for month in os.scandir(year):
                for jsons in glob.glob(os.path.join(month.path, '*.json')):

                    with open(jsons, mode='r') as currentFile:
                        data = currentFile.read().replace('\n', '')
                        p = json.loads(data)["average"]
                        av_power_y.append(p)
            av_power_y_num = Average(av_power_y)


            with open(os.path.join(year.path, 'average.json'), 'w') as f:
                av = {"average": av_power_y_num}
                f.write(json.dumps(av))
                f.close()

files_path = r"C:\Users\bsimb\Documents\Programmieren_Privat\Python\fronius eigen\ftp-direct\fronius\*.json"
ordner_path = r"C:\Users\bsimb\Documents\Programmieren_Privat\Python\json-to-ordnerstruct\test"

if __name__ == '__main__':
    move_files(files_path, ordner_path)
    add_averages_to_file_system(ordner_path)



