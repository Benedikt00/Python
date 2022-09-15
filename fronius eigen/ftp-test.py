import json
import os
import glob


p_List = []
path = 'C:/Users/bsimb/Documents/Programmieren_Privat/Python/fronius eigen/ftp-direct/fronius/'
for filename in glob.glob(os.path.join(path, '*.json')): #only process .JSON files in folder.
    with open(filename, encoding='utf-8', mode='r') as currentFile:
        data = currentFile.read().replace('\n', '')
        print(data)
        """
        keyword = json.loads(data)["keytolookup"]
        if keyword not in keywordList:
            keywordList.append(keyword)"""

        p = json.loads(data)["Body"]["Inverters"]["1"]["P"]
        p_List.append(p)

print(p_List)













