from playwright.sync_api import sync_playwright
from time import sleep
from bs4 import BeautifulSoup
import time
import os
import wetterdaten
from conveter import convertfromctox

def main():
    try:
        '''
        def restart():
            import sys
            print("argv was", sys.argv)
            print("sys.executable was", sys.executable)
            print("restart now")

            os.execv(sys.executable, ['python'] + sys.argv)
        '''


        #set a view system variables
        path = 'C:/Users/bsimb/Documents/Programmieren_Privat/Python/froniusneig/'

        var = "--- W"
        weather = 0

        status = "Running"

        akttime = time.localtime()
        stunden = time.strftime("%H", akttime)
        filedate = time.strftime("%d %m %y", akttime)
        filedate2 = time.strftime("%d. %B %Y", akttime)
        filename = "data " + str(filedate) + ".txt"

        #check if is the right time
        if int(stunden) >= 6 and int(stunden) <= 22:
            run = True
        else:
            run = False

        #main function
        if run:
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto('https://www.solarweb.com/PvSystems/PvSystem?pvSystemId=673dc46c-2863-4996-a638-a2480124484c')#go to solarweb page
                # region Login Daten
                page.fill('input#username', 'b.simbuerger@aon.at')
                page.fill('input#password', 'HTL@Benedikt1')#login
                # endregion
                page.click('button[type=button]')#anmelden

                #wait for page to load
                print("Progress ", end='')
                for x in range(5):
                    print(". ", end='')
                    sleep(1)
                print(".")

                html = page.content()#get page content
                soup = BeautifulSoup(html, 'html.parser')
                var = soup.find('span', {'style': 'white-space: nowrap; font-weight: 500;'}).text #searche for power in html
                var = convertfromctox(var)
                weather = wetterdaten.get_weather_data()
                browser.close() # close browser

            pathnew = path + filename

            isExist = os.path.exists(pathnew)

            # check if file already exists
            if isExist == False:
                newfile = open(filename, "a")

                newfile.close()

            wtf = open(pathnew, "a")

            aztime = time.strftime("%H:%M:%S %d. %m. %y", akttime)
            fvar = str(weather) + " " + str(aztime) + " " + str(var) + "\n"

            #writes data to file
            if var != "--- W":
                wtf.write(fvar)
            wtf.close()

            pathacdata = "C:/wamp64/www/fileupload-master/data/actdata.txt"

            #open the file for the data
            with open(pathacdata, 'r') as file:
                data = file.readlines()
            data[0] = str(var) + " W " + str(aztime) + "\n"
            data[1] = status


            # and write everything back
            with open(pathacdata, 'w') as file:
                file.writelines(data)

            print("Loop "+ str(aztime))

    except Exception as e:
        print(e)
        status = "ERROR"
        with open('C:/Users/bsimb/Documents/Programmieren_Privat/Python/froniusneig/actdata.txt', 'r') as file:
            # read a list of lines into data
            data = file.readlines()
        data[1] = status

        # and write everything back
        with open('C:/Users/bsimb/Documents/Programmieren_Privat/Python/froniusneig/actdata.txt', 'w') as file:
            file.writelines(data)

if __name__ == '__main__':
    main()

