import pygame
import pygame.freetype
import math

pygame.init()


wScreen = 1800
hScreen = 500

win = pygame.display.set_mode((wScreen, hScreen))

#programIcon = pygame.image.load('icon.png')

#pygame.display.set_icon(programIcon)
class rail():

    def __init__(self, point_1, point_2, color):

        if point_1[0] < point_2[0]:
            self.point_1 = list(point_1)
            self.point_2 = list(point_2)
        else:
            self.point_1 = list(point_2)
            self.point_2 = list(point_1)


        self.color = color

        self.point_between = (1, 1)

        self.point = {"p1.x": self.point_1[0], "p1.y": self.point_1[1], "p2.x": self.point_2[0], "p2.y": self.point_2[1]}

    def draw_line(self, point1, point2):
        Δx = abs(point2[0] - point1[0])
        Δy = abs(point2[1] - point1[1])

        if Δx > Δy:
            if point2[0] < point1[0]:
                self.point_between = [point2[0] + Δx - Δy, point2[1]]
            else:
                self.point_between = [point1[0] + Δy, point2[1]]

        else:
            if point1[1] < point2[1]:
                self.point_between = [point2[0], point1[1] + Δx] #Δy
            else:
                self.point_between = [point2[0], point1[1] - Δx]


        pygame.draw.line(win, self.color, (self.point_1[0], self.point_1[1]), self.point_between, 7)

        pygame.draw.line(win, self.color, self.point_between, (self.point_2[0], self.point_2[1]),7)

        pygame.draw.circle(win, self.color, (self.point_1[0], self.point_1[1]), 6)
        pygame.draw.circle(win, self.color, (self.point_2[0], self.point_2[1]), 6)


    def draw(self, win):
        self.draw_line(self.point_1, self.point_2)

    def get_3_points(self):
        return self.point_1, self.point_2, self.point_between

class train():
    def __init__(self):
        self.p = 70
        self.three_points = [[1, 2], [3, 4], [5, 6]]


    def XY(self, perc):
        """A = self.three_points[0]
        B = self.three_points[1]
        C = self.three_points[2]

        print(A)
        try:
            onepart = ((((B[0] - A[0]) + math.sqrt((C[0] - B[0])**2)*2)*self.p)-(B[0]-A[0])) * math.sin(math.degrees(45))
            self.relXY = (B[0] + onepart, B[1] + onepart)
        except ValueError:
            pass
        print(self.relXY, " des\n ",A, B, C)
        return self.relXY
"""

        A = self.three_points[0]
        C = self.three_points[1]
        B = self.three_points[2]
        a = B[0] - A[0]
        ro = C[1] - B[1]
        b = math.sqrt(2*(ro**2))
        ges = a+b
        prozent_mit_ges_laenge = (ges/100)*self.p
        laenge_on_b = ges - prozent_mit_ges_laenge - a
        x = laenge_on_b * math.sin(math.degrees(45))
        return [B[0] + x, B[1] + x]




    def calc_X_Y_from_percentage(self):

        """
                        *C
                       /|
                    d / | bY
        A          B /  |
        *__________*/___+
             a         bX
        """
        """self.p0 = self.three_points[0]
        self.p1 = self.three_points[1]
        self.p2 = self.three_points[2]


        A = self.p0
        B = self.p2
        C = self.p1



        bY = A[1] - C[1]

        bX = C[0] - B[0]

        #print(bY , " by bx", bX)

        d = math.sqrt(bY**2 + bX**2)
        a = B[0] - A[0]

        #print(a, " a d ", d)


        ges_len = a + d


        try:
            rel_len_a = (100*a)/ges_len
        except ZeroDivisionError:
            rel_len_a = 0

        if self.p > rel_len_a:
            position = (0, 0)
        elif self.p < rel_len_a:
            abs_len_on_a = (ges_len * rel_len_a)/100
            position = [A[1], abs_len_on_a]
        else:
            position = (0, 0)"""

        A = self.three_points[0]
        B = self.three_points[2]
        C = self.three_points[1]

        Δx = abs(C[0] - A[0])
        Δy = abs(C[1] - A[1])

        bY = Δy

        if Δx > Δy:
            # ---
            if A[1] > C[1]:
                if B[1] - 5 < A[1] < B[1] + 5:
                    #__/
                    pass
                elif B[1] - 5 < C[1] < B[1] + 5:
                    # __
                    #/
                    pass
            if A[1] < C[1]:
                if B[1] - 5 < A[1] < B[1] + 5:
                    # __
                    #   \
                    pass
                elif B[1] - 5 < C[1] < B[1] + 5:
                    # \__
                    pass

        else:
            # |
            # |
            if A[1] > C[1]:
                if B[0] - 5 < A[0] < B[0] + 5:
                    # /
                    #|
                    #|
                    print(" /\n|\n|\n")
                elif B[0] - 5 < C[0] < B[0] + 5:
                    # |
                    # |
                    #/
                    print(" |\n |\n/\n")
            if A[1] < C[1]:
                if B[0] - 5 < A[0] < B[0] + 5:
                    # |
                    # |
                    # \
                    print(" |\n|\n \ \n")
                elif B[0] - 5 < C[0] < B[0] + 5:
                    #\
                    # |
                    # |
                    print("\\\n |\n |\n")




            """if point1[1] < point2[1]:
                self.point_between = [point2[0], point1[1] + Δx]
            else:
                self.point_between = [point1[0], point2[1] + Δx]"""


    def draw(self):
        self.pos = self.XY(self.p)
        pygame.draw.circle(win, (255, 0, 0), self.pos, 6)

def redrawWindow():
    win.fill((255, 255, 255))
    line1.draw(win)
    train1.draw()
    pygame.display.update()

p1 = [100, 50]
p2 = [250, 250]
line1 = rail(p1, p2,  (0, 0, 0))
train1 = train()

run = True

print(line1.get_3_points())

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    train1.three_points = line1.get_3_points()

#Inputs
    keys = pygame.key.get_pressed()

    key_input = pygame.key.get_pressed()

    if key_input[pygame.K_w]:
        line1.point_1[1] -= 1

    if key_input[pygame.K_s]:
        line1.point_1[1] += 1

    if key_input[pygame.K_a]:
        line1.point_1[0] -= 1

    if key_input[pygame.K_d]:
        line1.point_1[0] += 1


    if key_input[pygame.K_UP]:
        line1.point_2[1] -= 1

    if key_input[pygame.K_DOWN]:
        line1.point_2[1] += 1

    if key_input[pygame.K_LEFT]:
        line1.point_2[0] -= 1

    if key_input[pygame.K_RIGHT]:
        line1.point_2[0] += 1


    redrawWindow()


pygame.quit()



