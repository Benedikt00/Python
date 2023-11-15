

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


#def sorthelp(el):
#    #av = (el[0][2] + el[1][2] + el[2][2])/3
#    #mx = []
#    #for i in range(len(el)):
#    #    mx.append(el[i][-1])
#
#    return (el[0][2] + el[1][2] + el[2][2])/3
#
#
#def sortListforZ(list):
#    what = list.sort(key=sorthelp, reverse=False)
#    #print(what)
#    return what

def sorthelp(el):
    return (el[0][2] + el[1][2] + el[2][2]) / 3

def sortListforZ(my_list):
    my_list.sort(key=sorthelp, reverse=True)
    return my_list


def Listaveraging(list):
    ar = ASSCI_StlToList(list)

    xAv = 0
    yAv = 0
    zAv = 0

    for x in range(len(ar)):
        for y in range(len(ar[x])):
            xAv += ar[x][y][0]
            yAv += ar[x][y][1]
            zAv += ar[x][y][2]

    xAv /= len(ar) * 3
    yAv /= len(ar) * 3
    zAv /= len(ar) * 3

    for x in range(len(ar)):
        for y in range(len(ar[x])):
            ar[x][y][0] -= xAv
            ar[x][y][1] -= yAv
            ar[x][y][2] -= zAv

    return ar


def STLtoList(list, averageing):
    if averageing:
        return Listaveraging(list)
    else:
        return ASSCI_StlToList(list)


def getSurfaceNormals(file):
    file = open(file)  # open File
    lines = file.readlines()
    cords = []
    for i in lines:
        if "facet normal" in i:  # leaves only the normals to use
            i = i[16:-1]
            i = i.split()
            cords.append(i)
    #convert to float
    for i in range(len(cords)):
        for j in range(len(cords[i])):

            cords[i][j] = float(str(cords[i][j]))

    return cords