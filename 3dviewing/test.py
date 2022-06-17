def ASSCI_StlToList(location):
    file = open(location) #open File
    lines = file.readlines()
    cords = []
    for i in lines:
        if "vertex" in i: #leaves only the cords to use
            i = i[16:-2] #removes unnecassary stuff
            cords.append(i)
    n = 0
    cl = []

    #brings everything to a list form
    for i in range(len(cords) // 3): #we pair things in 3
        tempList = []
        for j in range(3):
            cn = cords[n]
            tempList.append(cn.split())#neat thing to split the cords in lists
            n += 1
        cl.append(tempList)

    for i in range(len(cl)):
        for j in range(len(cl[i])):
            for k in range(len(cl[i][j])):
                cl[i][j][k] = float(cl[i][j][k])

    return cl


def sorthelp(el):
    av = (el[0][2] + el[1][2] + el[2][2])/3
    return av

def sortListforZ(list):
    list.sort(key=sorthelp)
    return list





def Listaveraging(list):
    ar = ASSCI_StlToList(list)

    l2d = []
    for e1 in ar:
        for e2 in e1:
            l2d.append(e2)

    ax = 0
    ay = 0
    az = 0

    for x in l2d:
        ax += x[0]
        ay += x[1]
        az += x[2]

    lenList = len(l2d)

    averageX = ax / lenList
    averageY = ay / lenList
    averageZ = az / lenList

    average = [averageX, averageY, averageZ]

    for i in range(len(l2d)):
        l2d[i][0] = l2d[i][0] - average[0]
        l2d[i][1] = l2d[i][1] - average[1]
        l2d[i][2] = l2d[i][2] - average[2]

    return l2d


def getSurfaceNormals(file):
    file = open(file)  # open File
    lines = file.readlines()
    cords = []
    for i in lines:
        if "facet normal" in i:  # leaves only the normals to use
            i = i[16:-2]
            i = i.split()
            cords.append(i)
    #convert to float
    for i in range(len(cords)):
        for j in range(len(cords[i])):
            cords[i][j] = float(cords[i][j])

    return cords