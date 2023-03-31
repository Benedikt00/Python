import random
from PIL import Image
from datetime import datetime
import os

#mydir = R"C:\Users\bsimb\Documents\Programmieren_Privat\Python\WaveFunctionCollapse"
#for f in os.listdir(mydir):
#    if not f.endswith(".jpg"):
#        continue
#    os.remove(os.path.join(mydir, f))


TUp = Image.open("Icons/1.bmp")
TRight = Image.open("Icons/2.bmp")
TDown = Image.open("Icons/3.bmp")
TLeft = Image.open("Icons/4.bmp")

LUp = Image.open("Icons/5.bmp")
LRight = Image.open("Icons/6.bmp")
LDown = Image.open("Icons/7.bmp")
LLeft = Image.open("Icons/8.bmp")

PWhite = Image.open("Icons/white.bmp")

FTUp = [TUp,
        {"Top": [TRight, TLeft, TDown, LDown, LLeft], "Right": [TUp, TLeft, TDown, LUp, LLeft], "Bottom": [TDown, LDown, LLeft], "Left": [TUp, TRight, TDown, LDown, LRight]}]
FTRight = [TRight,
           {"Top": [TRight, TLeft, TDown, LDown, LLeft], "Right": [TUp, TLeft, TDown, LUp, LLeft], "Bottom": [TUp, TRight, TLeft, LUp, LRight], "Left": [TLeft, LUp, LLeft]}]
FTDown = [TDown,
          {"Top": [TUp, LUp, LRight], "Right": [TUp, TLeft, TDown, LUp, LLeft], "Bottom": [TUp, TRight, TLeft, LUp, LRight], "Left": [TUp, TRight, TDown, LRight, LDown]}]
FTLeft = [TLeft,
          {"Top": [TRight, TLeft, TDown, LDown, LLeft], "Right": [TRight, LRight, LDown], "Bottom": [TRight, TUp, TLeft, LRight], "Left": [TRight, TDown, LRight, LDown]}]


FLUp = [LUp, {"Top": [TRight, TLeft, TDown, LDown, LLeft], "Right": [TRight, LRight, LDown], "Bottom": [TDown, LDown, LLeft], "Left": [TRight, TUp, TDown, LRight, LDown]}]

FLRight = [LRight, {"Top": [TRight, TLeft, TDown, LDown, LLeft], "Right": [TUp, TLeft, TDown, LUp, LLeft], "Bottom": [TDown, LDown, LLeft], "Left": [TLeft, LUp, LLeft]}]

FLDown = [LDown, {"Top": [TUp, LUp, LRight], "Right": [TUp, TLeft, TDown, LUp, LLeft], "Bottom": [TUp, TRight, TLeft, LUp, LRight], "Left": [TLeft, LLeft, LUp]}]

FLLeft = [LLeft,
          {"Top": [TUp, LRight, LUp], "Right": [TRight, LRight, LDown, ], "Bottom": [TRight, TUp, TLeft, LUp, LRight], "Left": [TUp, TDown, TRight, LRight, LDown]}]


White = [PWhite, []]


def convertAddressToString(listAdress):
    listReturn = []
    listAllTilesName = ["TUp", "TRight", "TDown", "TLeft", "LUp", "LRight", "LDown", "LLeft"]
    for address in listAdress:
        for i, addr in enumerate(AllTiles):
            if address == addr:
                listReturn.append(listAllTilesName[i])
    return listReturn


AllTiles = [TUp, TRight, TDown, TLeft, LUp, LRight, LDown, LLeft]
AllTiles_ = [FTUp, FTRight, FTDown, FTLeft, FLUp, FLRight, FLDown, FLLeft]

GridSize = [64, 64]
image_size = [16, 16]

allTiles = GridSize[0] * GridSize[1]

Positions = []
for i in range(GridSize[0]):
    tmp = []
    for j in range(GridSize[1]):
        tmp.append([])
    Positions.append(tmp)

for i, el in enumerate(Positions):
    for j, el2 in enumerate(el):
        Positions[i][j] = White

new_image = Image.new('RGB', (GridSize[0] * image_size[0], GridSize[1] * image_size[1]))


def getRandomTile(avaliable):
    if len(avaliable) != 0:
        return avaliable[random.randrange(0, len(avaliable))]
    else:
        draw()
        exit(code="Len Avaliable == 0")

def firstTile():
    randx = random.randint(0, GridSize[0] - 1)
    randy = random.randint(0, GridSize[1] - 1)
    Positions[randx][randy] = getRandomTile(AllTiles_)
    print("First Tile: ", randx, " ", randy)
    return randx, randy


def draw():
    for i, el in enumerate(Positions):
        for j, el2 in enumerate(el):
            new_image.paste(el2[0], (image_size[0] * i, image_size[1] * j))

    now = datetime.now()

    current_time = now.strftime("%H_%M_%S_%f")
    name = "./img_" + current_time + ".jpg"
    new_image.save(name, "JPEG")


def TilesFilled():
    filledTiles = []
    for i in range(GridSize[0]):
        for j in range(GridSize[1]):
            if Positions[i][j] != White:
                filledTiles.append([i, j])
    return filledTiles


def SortEntropy(filledTiles):
    TilesAfterEntropy = [[], [], [], [], []]
    for i in range(len(Positions)):
        for j in range(len(Positions[i])):
            if [i, j] not in filledTiles:
                ent = 0
                if i > 0:
                    TileTop = Positions[i - 1][j]
                    if (TileTop != White) and Positions[i - 1][j]:
                        ent += 1
                if j < GridSize[1] - 1:
                    TileRight = Positions[i][j + 1]
                    if (TileRight != White) and Positions[i][j + 1]:
                        ent += 1
                if i < GridSize[0] - 1:
                    TileBottom = Positions[i + 1][j]
                    if (TileBottom != White) and Positions[i + 1][j]:
                        ent += 1
                if j > 0:
                    TileLeft = Positions[i][j - 1]
                    if (TileLeft != White) and Positions[i][j - 1]:
                        ent += 1

                TilesAfterEntropy[ent].append([i, j])
    return TilesAfterEntropy


def ChooseToCollapse(tilesAfterEntropy):
    tilesAfterEntropy = [x for x in tilesAfterEntropy if x != []]
    Pos = random.choice(tilesAfterEntropy[-1])
    return Pos


def Collapse(Pos):
    tiles_to_choose = AllTiles
    y = Pos[0]
    x = Pos[1]
    #print("x y", x, y)
    if y > 0:
        #print("y > 0")
        if Positions[y - 1][x] != White:
            tilesTemp = []
            #print("Left Tile",  convertAddressToString(Positions[y - 1][x][1]["Right"]), y-1, x)
            for Tile in Positions[y - 1][x][1]["Right"]:
                if Tile in tiles_to_choose:
                    tilesTemp.append(Tile)
            tiles_to_choose = tilesTemp

    if y < GridSize[0] - 1:
        #print("y < 15")
        if Positions[y + 1][x] != White:
            #print("Right Tile",  convertAddressToString(Positions[y + 1][x][1]["Left"]), y+1, x)
            tilesTemp = []
            for Tile in Positions[y + 1][x][1]["Left"]:
                if Tile in tiles_to_choose:
                    tilesTemp.append(Tile)
            tiles_to_choose = tilesTemp

    if x > 0:
        #print("x > 0")
        if Positions[y][x - 1] != White:
            #print("Top Tile",  convertAddressToString(Positions[y][x - 1][1]["Bottom"]), y, x-1)
            tilesTemp = []
            for Tile in Positions[y][x - 1][1]["Bottom"]:
                if Tile in tiles_to_choose:
                    tilesTemp.append(Tile)
            tiles_to_choose = tilesTemp

    if x < GridSize[1] - 1:
        #print("y < 15")
        if Positions[y][x + 1] != White:
            #print("Bottom Tile", convertAddressToString(Positions[y][x + 1][1]["Top"]), y, x+1)
            tilesTemp = []
            for Tile in Positions[y][x + 1][1]["Top"]:
                if Tile in tiles_to_choose:
                    tilesTemp.append(Tile)
            tiles_to_choose = tilesTemp

    #print("Tiles to choose from: ", convertAddressToString(tiles_to_choose))
    Pic = getRandomTile(tiles_to_choose)
    #print("Choosen:", convertAddressToString([Pic]))
    return Pic


def setTile(Pic, Pos):
    for Tile in AllTiles_:
        if Pic in Tile:
            Positions[Pos[0]][Pos[1]] = Tile
            return


def isFinished():
    for el in Positions:
        for el2 in el:
            if el2 == White:
                return False
    return True


var = 1

cordsfirst = firstTile()

while not isFinished():
    fillledTiles = TilesFilled()
    listEntropy = SortEntropy(fillledTiles)
    #print("List Entropy:", listEntropy, "\n")
    PosToCollapse = ChooseToCollapse(listEntropy)
    #print("Position to Collapse:", PosToCollapse, "\n")
    Pic = Collapse(PosToCollapse)
    setTile(Pic, PosToCollapse)
    var += 1
    print(str(var) + "/" + str(allTiles))
draw()
# sleep(1)
