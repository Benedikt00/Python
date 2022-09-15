import json
import os
import glob
import weather
import time
import asyncio

# function to add to JSON
def write_json(new_data, filename):
    with open(filename, 'r+') as file:
        # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.update(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=4)


path = 'C:/Users/bsimb/Documents/Programmieren_Privat/Python/fronius eigen/ftp-direct/fronius/'

list_of_files = glob.glob('C:/Users/bsimb/Documents/Programmieren_Privat/Python/fronius eigen/ftp-direct/fronius/*.json') # * means all if need specific format then *.csv

async def start_data(start_now=False):
    # this makes program sleep in intervals
    from time import time, sleep
    import datetime
    while True:

        now = datetime.datetime.now()

        if start_now:
            list_of_files = glob.glob(
                'C:/Users/bsimb/Documents/Programmieren_Privat/Python/fronius eigen/ftp-direct/fronius/*.json')
            try:
                latest_file = max(list_of_files, key=os.path.getctime)
                y = {"weather":
                    {
                        "sky": weather.get_weather_data(in_num = False)
                    }
                }
                print("Writing . . .")
                print(y)
                write_json(y, latest_file)
            except ValueError:
                print("File without Weather got created:")
                print()

        if now.minute == 1 or now.minute == 11 or now.minute == 21 or now.minute == 31 or now.minute == 41 or now.minute == 51:
            list_of_files = glob.glob(
                'C:/Users/bsimb/Documents/Programmieren_Privat/Python/fronius eigen/ftp-direct/fronius/*.json')
            try:
                latest_file = max(list_of_files, key=os.path.getctime)
                y = {"weather":
                    {
                        "sky": weather.get_weather_data(in_num = False)
                    }
                }
                print("Writing . . .")
                print(y)
                write_json(y, latest_file)
            except ValueError:
                print("File without Weather got created:")
                print(latest_file)


            sleep(120)
        sleep(5)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_data(False))

















