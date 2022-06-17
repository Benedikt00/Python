import pygame
import math

pygame.init()

wScreen = 1800
hScreen = 500

gew1 = 30
gew2 = 30

def regulation(g1, g2):
    g1 = math.sqrt(g1 ** 2)
    g2 = math.sqrt(g2 ** 2)

    gq = g1+g2
    gtl = gq * 0.0001

    ga1 = g1/gtl
    ga2 = g2/gtl
    return(ga1, ga2)

gges = regulation(gew1, gew2)

massbox1 = gges[0]
massbox2 = gges[1]


startvel1 = 5
startvel2 = -2

def regulation(w1, w2):
    w1 = math.sqrt(w1 ** 2)
    w2 = math.sqrt(w2 ** 2)

    wq = w1+w2
    tl = wq * 2

    wa1 = w1/tl
    wa2 = w2/tl
    return(wa1, wa2)

wn2 = regulation(startvel1, startvel2)

power_ebox = wn2[0]
power_zbox = wn2[1] * (-1)

hightbox1 = math.sqrt(massbox1)*3
hightbox2 = math.sqrt(massbox2)*3

win = pygame.display.set_mode((wScreen, hScreen))

class box(object):
    def __init__(self,x , hight, color):
        self.x = x

        self.hight = hight
        self.color = color

    def draw (self, win):
        pygame.draw.rect(win, (0, 0, 0), pygame.Rect(self.x, 440 - self.hight, self.hight, self.hight))
        pygame.draw.rect(win, (self.color), pygame.Rect(self.x + 2, 440 - self.hight + 2, self.hight - 4, self.hight - 4))

def pathbox(startx, power, time):

    #distx = power * time
    newx = startx + power

    return(newx)



def poweraftercollision(boxpower):
    m1 = massbox1
    v1 = power_ebox
    m2 = massbox2
    v2 = power_zbox

    vs = (((m1*v1)+(m2*v2))/(m1+m2))

    un = (2*vs) - boxpower
    print(un)
    return un


velo1 = "0"


def redrawWindow():
    win.fill((33, 114, 219))
    ebox.draw(win)
    zbox.draw(win)
    win.blit(text, (30, 30))
    pygame.display.update()

font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(velo1, True, (0, 0, 0))
textRect = text.get_rect()

ebox = box(100,  round(hightbox1), (75, 131, 235))
zbox = box(wScreen - hightbox2 - 100,  round(hightbox2), (214, 26, 51))

time = 0
timeincromenz = 0.0001

secpow1 = 0
secpow2 = 0


run = True
collacured = False


while run:

    if not collacured:
        if zbox.x > (0 - zbox.hight) or ebox.x < wScreen:
            time += timeincromenz
            po_e = pathbox(ebox.x, power_ebox, time)
            ebox.x = po_e
            velo1 = str(power_ebox)
            text = font.render(velo1, True, (0, 0, 0))

            po_z = pathbox(zbox.x, power_zbox, time)
            zbox.x = po_z

        if zbox.x <= ebox.x + ebox.hight:
            collacured = True
            secpow1 = poweraftercollision(power_ebox)
            secpow2 = poweraftercollision(power_zbox)

    if collacured and (zbox.x > (0 - zbox.hight) or ebox.x < wScreen):
        time += timeincromenz

        po_e = pathbox(ebox.x, secpow1, time)
        ebox.x = po_e

        po_z = pathbox(zbox.x, secpow2, time)
        zbox.x = po_z

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    redrawWindow()





