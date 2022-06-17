
def convertfromctox(strnum):#converts 1kW in 1000W
    strnum = strnum[:-1] #erases the "W"
    if (strnum.find('k')) != -1: #checks if there is a k in the string
        #converts it to W
        strnum = strnum[:-1]
        num = float(strnum.replace(',', '.'))
        num = num * 1000
        num = round(num)
    else:
        num = int(strnum)

    return num
