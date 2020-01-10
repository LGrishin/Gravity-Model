from math import *
from time import *
from tkinter import *  
from collections import deque
import pygame

G = 6.67408*10**-11
run = True
t = 0.3
n = 1
step = 2
count = 2
MainArray = []
Div = 1
DIV = 1
m = True 
TrDepth = 600
BLACK = (0, 0, 0)
k = 4
SIZE = False
ButMass = []
def Module (x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def Module1 (a, b):
    return sqrt((a)**2 + (b)**2)

def angle (x1, y1, x2, y2):
    if x1 - x2 != 0 :
        f = atan((y1 - y2) / (x1 - x2))
    if y1 == y2:
        if x1>x2:
            return pi
        else :
            return 0
    if x1 == x2:
        if y1 > y2:
            return - pi / 2
        else :
            return pi / 2

    if x1 <= x2 and y1 <= y2:
        return f
    if x1 > x2 and y1 > y2:
        return  pi + f
    if x1 >= x2 and y1 <= y2: 
        return pi + f
    if x1 < x2 and y1 > y2:
        return f

def Force (m1, m2, x1, y1, x2, y2, var):
    angle1 = angle(x1, y1, x2, y2)
    F = ((G * m1 * m2) / (Module(x1, y1, x2, y2))**2)
    Fx = F * cos(angle1)
    Fy = F * sin(angle1)
    if var == 0:
        return F
    if var == 1:
        return Fx
    if var == 2:
        return Fy

def CoordinateX (x0, Vx, t):
    return Vx * t + x0
 
def CoordinateY (y0, Vy, t):
    return Vy * t + y0
 
def VelocityX (Ax, Vx, t):
    return Ax * t + Vx

def VelocityY (Ay, Vy, t):
    return Ay * t + Vy

def Acceleration (F, Fx, Fy, m, var):
    if var == 0:
        return F/m
    if var == 1:
        return Fx / m
    if var == 2:
        return Fy / m

def AccelerationC (V, R):
    return (V ** 2) / R

def OrbVel(m, x1, y1, x2, y2):
    global G
    h = Module(x1, y1, x2, y2)
    return sqrt(G * (m / h))

def EscVel(m, x1, y1, x2, y2):
    return sqrt(2) * OrbVel(m, x1, y1, x2, y2)

def Collision(m1, m2, Vx1, Vy1, Vx2, Vy2, var):
    Vx = (Vx1 * m1 + Vx2 * m2) / (m1 + m2)
    Vy = (Vy1 * m1 + Vy2 * m2) / (m1 + m2)
    V = Module1(Vx, Vy)
    if var == 0:
        return V
    if var == 1:
        return Vx
    if var == 2: 
        return Vy

def Shift (A, n):
    d = deque(A[n])
    d.rotate(1)
    return d

def ShiftPoint (A, n, dc, TrDepth, k):
    for M1 in range (k):
        for M2 in range (TrDepth):
            if n == 0:
                Trajectory[M1][M2] =(Trajectory[M1][M2] [0]  + dc, Trajectory[M1][M2][1]) 
            else:
                Trajectory[M1][M2] =(Trajectory[M1][M2] [0] , Trajectory[M1][M2][1]  + dc)
    return A

def RestoreMyUniverse (k , TrDepth, MainArray):
    for j in range (k):
        for z in range (TrDepth):
            pygame.draw.rect(sc, (255, 255, 255) , (int(Trajectory[j][z][0] / DIV ), int(Trajectory[j][z][1]) / DIV , 1, 1))
        pygame.draw.circle(sc, MainArray[j].color, (int(MainArray[j].x0 / DIV ), int(MainArray[j].y0 / DIV) ), int(MainArray[j].r / DIV), 0)
        pygame.display.update()


def DrawVec (p):
    pygame.draw.circle(sc, MainArray[p].color, (x1[p], y1[p]), MainArray[p].r)
    pygame.draw.aaline(sc, DrawOrbVel(p, x2[p] - x1[p], y2[p] - y1[p]), [x1[p], y1[p]], [x2[p], y2[p]])
    pygame.draw.aaline(sc, DrawOrbVel(p, x2[p] - x1[p], y2[p] - y1[p]), [x2[p], y2[p]], [x2[p]  - 10 * cos(angle(x1[p], y1[p], x2[p], y2[p]) - pi / 8) , y2[p] - 10 *sin(angle(x1[p], y1[p], x2[p], y2[p]) - pi / 8)])
    pygame.draw.aaline(sc, DrawOrbVel(p, x2[p] - x1[p], y2[p] - y1[p]), [x2[p], y2[p]], [x2[p]  - 10 * cos(angle(x1[p], y1[p], x2[p], y2[p]) + pi / 8) , y2[p] - 10 *sin(angle(x1[p], y1[p], x2[p], y2[p]) + pi / 8)])
    pygame.display.update()

def DrawMyUniverse (p):
    pygame.draw.aaline(sc, (255, 255, 255), [x1[p], y1[p]], [x2[p], y2[p]])
    pygame.draw.aaline(sc, (255, 255, 255), [x2[p], y2[p]], [x2[p]  - 10 * cos(angle(x1[p], y1[p], x2[p], y2[p]) - pi / 8) , y2[p] - 10 *sin(angle(x1[p], y1[p], x2[p], y2[p]) - pi / 8)])
    pygame.draw.aaline(sc, (255, 255, 255), [x2[p], y2[p]], [x2[p]  - 10 * cos(angle(x1[p], y1[p], x2[p], y2[p]) + pi / 8) , y2[p] - 10 *sin(angle(x1[p], y1[p], x2[p], y2[p]) + pi / 8)])
    pygame.draw.circle(sc, MainArray[p].color, [x1[p], y1[p]], MainArray[p].r)
    pygame.display.update()

def g (m, h):
    global G
    return (G * m) / h

def RotTheCoorSys (x0, y0, x1, y1, x2, y2):
    alpha = angle(x1, y1, x2, y2)
    return (x0 * cos(alpha) + y0 * sin(alpha), - x0 * sin(alpha) + y0 * cos(alpha))

def DrawOrbVel (p, Vx, Vy):
    global  x1, x2, y1, y2
    if p == 1:
        Vx = ((x2[p] - x1[p]) / 10) - MainArray[p - 1].Vx
        Vy = ((y2[p] - y1[p])  / 10 ) - MainArray[p - 1].Vy
        print(MainArray[0].OrbVel)
        V = Module1(Vx, Vy)
        if V <= MainArray[0].OrbVel:
            return (255, 0, 0)
        if V > MainArray[0].OrbVel and V < MainArray[0].OrbVel * sqrt(2) :
            return (0, 0, 255)
        if V >= MainArray[0].OrbVel * sqrt(2):
            return (0, 255, 0)
    else:
        return (255, 255, 255)

def ColorForInf (r, i):
    global k
    if r == k:
        return (255, 255, 255)
    if r % k == i:
        return (0, 0, 255)    
    return (255, 255, 255)

def But1 (event):
    first_block.EntTheNum()

class Planet:
    x0 = 0
    y0 = 0
    Vx = 0
    Vy = 0
    V = Module1(Vx, Vy)
    Ax = 0
    Ay = 0
    A = Module1(Ax, Ay)
    Fx = 0
    Fy = 0
    F = Module1(Fx, Fy)
    m = 1
    OrbVel = 0
    r = 10
    ro = 9000000000
    color = (255, 0, 0) #color = (200, 0, 255)
    Col = False
    def Size(self, m, ro):
        self.r = ((3 * m) / (4 * pi * ro)) ** (1 / 3)
        if self.r > 10 and self. r < 16:
            self.color = (150, 0, 0)
        if self. r >= 16 :
            self.color = (80, 0, 0)
    def dS(self, Col):
        self.Col = Col
    def Color(self, color):
        self.color = color
    def Coor(self, x0, y0):
        self.x0 = x0
        self.y0 = y0
    def Vel(self, Vx, Vy):
        self.Vx = Vx
        self.Vy = Vy
        self.V = Module1(Vx, Vy)
    def Acc(self, Ax, Ay):
        self.Ax = Ax
        self.Ay = Ay 
        self.A = Module1(Ax, Ay)
    def Forc(self, Fx, Fy):
        self.Fx = Fx
        self.Fy = Fy
        self.F = Module1(Fx, Fy)
    def OVel(self, x, y):
        self.OrbVel = OrbVel(self.m, self.x0, self.y0, x, y)

class Block:
    p = 0
    cond = 0
    def __init__(self, master):
        self.e = Entry(master, width = 12)
        self.b = Button(master, text = "Enter", width = 10)
        self.e.pack()
        self.b.pack()
    def setFunc(self, func):
        self.b['command'] = eval('self.' + func)	
    def EntTheNum(self):
        global k
        m = 0
        m = int(self.e.get())
        if m > 1:
            k = m
        if m < -1:
            k = -m
    def EntTheMass(self):
        global MainArray
        MainArray[self.p].m = float(self.e.get()) * 10**9
    def dPi(self, p):
        self.p = p
    def dCond(self):
        self.cond += 1
    def Mass(self):
        if self.cond == 0:
            self.lab = Label(text = 'Введите количество объектов', font = ("Comic Sans MS", 10, "bold"))
        else:
            self.lab= Label(text = 'Введите массу ' + str(self.p + 1) + ' объекта', font = ("Comic Sans MS", 10, "bold"))
        self.lab.pack()
        
root = Tk()
lab = Label(text = 'Введите количество объектов', font = ("Comic Sans MS", 10, "bold"))
lab.pack()
first_block = Block(root)
root.bind('<Return>', But1)
first_block.setFunc('EntTheNum')
Button(root, text = "Next", command = root.destroy, width = 10).pack()
root.mainloop()

if k > 0:
    root = Tk()
    MainArray = [0] * k
    ButMass = [0] * k
    for i in range (k):
        MainArray.append(0)
    for i in range (k):
        MainArray[i] = Planet()
    for i in range (k):
        ButMass[i] = Block(root)
        ButMass[i].dPi(i)
        ButMass[i].dCond()
        ButMass[i].Mass()
    for i in range (k):
        ButMass[i].setFunc('EntTheMass')
    Button(root, text = "Next", command = root.destroy).pack()
    root.mainloop()

for i in range (k):
    MainArray.append(0)
for i in range (k):
    MainArray[i] = Planet()

MainArray[0].m = 9*10**15
MainArray[1].m = 9*10**9
MainArray[2].m = 9*10**8
MainArray[3].m = 9*10**4

x1 = [-10000]  * k
y1 = [-10000]  * k
x2 = [-10000]  * k
y2 = [-10000]  * k

Trajectory = [[0] * TrDepth for i in range(k)]
for i in range (k):
    for j in range (TrDepth):
        Trajectory[i][j] = (0, 0)

pygame.init()
clock = pygame.time.Clock()
w = pygame.display.set_mode((1920, 1110), pygame.RESIZABLE)
pygame.display.set_caption('WWW')
bg = pygame.image.load("5.jpg")
sc = pygame.Surface((1920, 1080))
inform = pygame.Surface((0, 0))
w.blit(sc, (0, 0))
sc.blit(bg, (0, -150))
pygame.display.flip()
#sound1 = pygame.mixer.Sound('Magic_Stick.wav')

p =-1

pygame.key.set_repeat(300, 10)

while run and p < k:
    w.blit(sc, (0, 0))
    pygame.display.flip()
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if  i.type ==  pygame.KEYDOWN:
            if i.key == pygame.K_SPACE:
                n += 1
        if n % 2 == 0:
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if p > -1  and p < k:
                        MainArray[p].Vel((x2[p] - x1[p]) / 10, (y2[p] - y1[p]) / 10)
                    p += 1
                    if   p < k:
                        if p == 1:
                            MainArray[0].OVel(MainArray[1].x0, MainArray[1].y0)                                                    
                        pygame.draw.circle(sc, MainArray[p].color, i.pos, MainArray[p].r)
                        MainArray[p].Coor(i.pos[0], i.pos[1])
                        pygame.display.update()
                        x1[p] = i.pos[0]
                        y1[p] = i.pos[1]
                        x2[p] = i.pos[0]
                        y2[p] = i.pos[1]
                if i.button == 3:
                    step += 1
                    if step % 2 == 0:
                        Div = 1
                    if step % 2 != 0:
                        Div = 10

            if  i.type ==  pygame.KEYDOWN:
                if i.key == pygame.K_LEFT:
                    DrawVec(p)
                    w.blit(sc, (0, 0))                    
                    sc.blit(bg, (0, -150))
                    x2[p] -= 10 / Div
                    for j in range (p):
                        DrawMyUniverse(j)
                    DrawVec (p)

                if i.key == pygame.K_RIGHT:
                    x2[p] += 10 / Div 
                    w.blit(sc, (0, 0))
                    sc.blit(bg, (0, -150))
                    for j in range (p):
                        DrawMyUniverse(j)
                    DrawVec (p)


                if i.key == pygame.K_UP:
                    y2[p] -= 10 / Div
                    w.blit(sc, (0, 0))
                    sc.blit(bg, (0, -150))
                    for j in range (p):
                        DrawMyUniverse(j)
                    DrawVec (p)

                if i.key == pygame.K_DOWN:
                    y2[p] += 10 / Div
                    w.blit(sc, (0, 0))
                    sc.blit(bg, (0, -150))
                    for j in range (p):
                        DrawMyUniverse(j)
                    DrawVec (p)

        if n%2 != 0:
            if i.type == pygame.MOUSEBUTTONDOWN:
                if i.button == 1:
                    if p > -1  and p < k:
                        MainArray[p].Vel((x2[p] - x1[p]) / 10, (y2[p] - y1[p]) / 10)
                    if p < 0 or count %2 == 0 :
                        p += 1
                    if   p < k  and count %2 == 0:
                        pygame.draw.circle(sc, MainArray[p].color, i.pos, MainArray[p].r)
                        MainArray[p].Coor(i.pos[0], i.pos[1])
                        if p == 1:
                            MainArray[0].OVel(MainArray[1].x0, MainArray[1].y0)
                        pygame.display.update()
                        x1[p] = i.pos[0]
                        y1[p] = i.pos[1]
                        x2[p] = i.pos[0]
                        y2[p] = i.pos[1]
                    count += 1
                if i.button == 3:
                    step += 1
                    if step % 2 == 0:
                        Div = 1
                    if step % 2 != 0:
                        Div = 10
            if i.type == pygame.MOUSEMOTION:
                if count %2 != 0 and p < k:
                    x2[p] = i.pos[0]
                    y2[p] = i.pos[1]
                    w.blit(sc, (0, 0))
                    sc.blit(bg, (0, -150))
                    for j in range (p):
                        DrawMyUniverse(j)
                    DrawVec (p)
    pygame.time.delay(40)
pygame.font.init()

Int_font = pygame.font.SysFont('Comic Sans MC', 20, False, True )
CS = 40
q = 0
Inf = False
ColorR = k
pygame.key.set_repeat(80, 10)
while run:
    w.blit(sc, (q, 0))
    sc.blit(bg, (0, -150))    
    if Inf:
        if q < 200:
            q += 5
            inform = pygame.Surface((q, 1080))
        w.blit(inform, (0, 0))
        inform.fill(BLACK)
    else:
        if q > 0:
            q -= 5
            inform = pygame.Surface((q, 1080))
        w.blit(inform, (0, 0))
        inform.fill(BLACK)
    inform.blit(Int_font.render(u'Time interval:  ' + str(t), 1, (255, 255, 255)), (0, 0))        
    for i in range (k):
        inform.blit(Int_font.render(u'Object  ' + str(i + 1) + ':', 1, ColorForInf(ColorR, i)), (0, 20 + 120 * i ))
        inform.blit(Int_font.render(u'm:  ' + str(MainArray[i].m), 1, (255, 255, 255)), (0, 40 + 120 * i ))        
        inform.blit(Int_font.render(u'Vx  ' + str(MainArray[i].Vx), 1, (255, 255, 255)), (0, 60 + 120 * i ))
        inform.blit(Int_font.render(u'Vy:  ' + str(MainArray[i].Vy), 1, (255, 255, 255)), (0, 80 + 120 * i ))
        inform.blit(Int_font.render(u'Ax:  ' + str(MainArray[i].Ax), 1, (255, 255, 255)), (0, 100 + 120 * i ))
        inform.blit(Int_font.render(u'Ay:  ' + str(MainArray[i].Ay), 1, (255, 255, 255)), (0, 120 + 120 * i ))
        for z in range (TrDepth):
            pygame.draw.rect(sc, (255, 255, 255) , (int(Trajectory[i][z][0] / DIV), int(Trajectory[i][z][1] / DIV), 1, 1))

    for i in range (k):
        if MainArray[i].Col == True and m == True:
            MainArray[i].m = 0
            MainArray[i].x0 = 0
            MainArray[i].y0 = 0
        MainArray[i].Fx = 0
        MainArray[i].Fy = 0
        for j in range (k):
            if i != j:
                if MainArray[i].Col != True:
                    MainArray[i].Fx += Force(MainArray[i].m, MainArray[j].m, MainArray[i].x0, MainArray[i].y0, MainArray[j].x0, MainArray[j].y0, 1)
                    MainArray[i].Fy += Force(MainArray[i].m, MainArray[j].m, MainArray[i].x0, MainArray[i].y0, MainArray[j].x0, MainArray[j].y0, 2)
                    MainArray[i].Forc(MainArray[i].Fx, MainArray[i].Fy)                    
                    if Module(MainArray[i].x0, MainArray[i].y0, MainArray[j].x0, MainArray[j].y0) <= MainArray[i].r + MainArray[j].r and m == True:
                        if MainArray[i].m > MainArray[j].m:
                            MainArray[i].x0 = CoordinateX (MainArray[i].x0, MainArray[i].Vx, t)
                            MainArray[i].y0 = CoordinateY (MainArray[i].y0, MainArray[i].Vy, t) 
                        else:
                            MainArray[i].x0 = CoordinateX (MainArray[j].x0, MainArray[j].Vx, t)
                            MainArray[i].y0 = CoordinateY (MainArray[j].y0, MainArray[j].Vy, t) 
                        MainArray[i].Vx = Collision(MainArray[i].m, MainArray[j].m, MainArray[i].Vx, MainArray[i].Vy, MainArray[j].Vx, MainArray[j].Vy, 1)
                        MainArray[i].Vy = Collision(MainArray[i].m, MainArray[j].m, MainArray[i].Vx, MainArray[i].Vy, MainArray[j].Vx, MainArray[j].Vy, 2)
                        MainArray[i].Vel(MainArray[i].Vx, MainArray[i].Vy)
                        MainArray[i].m += MainArray[j].m
                        MainArray[i].color = (((MainArray[i].color[0] + MainArray[j].color[0]) / 4) * 1.5, ((MainArray[i].color[1] + MainArray[j].color[1])/4)* 1.5, ((MainArray[i].color[2] + MainArray[j].color[2])/4)* 1.5)
                        MainArray[j].color = (0, 0, 0)
                        MainArray[i].dS(False)
                        MainArray[j].dS(True)
                        for Tr1 in range(TrDepth):
                            Trajectory[j][Tr1] = (0, 0)
        if MainArray[i].Col != True:
            MainArray[i].Ax = Acceleration(MainArray[i].F, MainArray[i].Fx, MainArray[i].Fy, MainArray[i].m, 1)
            MainArray[i].Ay = Acceleration(MainArray[i].F, MainArray[i].Fx, MainArray[i].Fy, MainArray[i].m, 2)
            MainArray[i].Vx = VelocityX(MainArray[i].Ax, MainArray[i].Vx, t)
            MainArray[i].Vy = VelocityY(MainArray[i].Ay, MainArray[i].Vy, t)
            MainArray[i].x0 = CoordinateX (MainArray[i].x0, MainArray[i].Vx, t)
            MainArray[i].y0 = CoordinateY (MainArray[i].y0, MainArray[i].Vy, t)
            MainArray[i].Coor(MainArray[i].x0, MainArray[i].y0)
            MainArray[i].Vel(MainArray[i].Vx, MainArray[i].Vy)
            MainArray[i].Acc(MainArray[i].Ax, MainArray[i].Ay)
            Trajectory[i] = Shift(Trajectory, i)
            Trajectory[i][0] = (MainArray[i].x0, MainArray[i].y0)
            if SIZE:
                MainArray[i].Size(MainArray[i].m, MainArray[i].ro)
            else:
                MainArray[i].r = 10
                MainArray[i].color = (255, 0, 0)
            pygame.draw.circle(sc, MainArray[i].color, (int(MainArray[i].x0 / DIV), int(MainArray[i].y0 / DIV )), int(MainArray[i].r / DIV), 0)

        pygame.display.flip()    
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        if  i.type ==  pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                for l in range (k):
                    MainArray[l].x0 += CS
                ShiftPoint(Trajectory, 0, CS, TrDepth, k)
                sc.blit(bg, (0, -150))
                RestoreMyUniverse(k, TrDepth, MainArray)

            if i.key == pygame.K_RIGHT:
                for l in range (k):
                    MainArray[l].x0 -= CS
                ShiftPoint(Trajectory, 0, -CS, TrDepth, k)
                sc.blit(bg, (0, -150))
                RestoreMyUniverse(k, TrDepth, MainArray)

            if i.key == pygame.K_UP:
                for l in range (k):
                    MainArray[l].y0 += CS
                ShiftPoint(Trajectory, 1, CS, TrDepth, k)
                sc.blit(bg, (0, -150))
                RestoreMyUniverse(k, TrDepth, MainArray)

            if i.key == pygame.K_DOWN:
                for l in range (k):
                    MainArray[l].y0 -= CS
                ShiftPoint(Trajectory, 1, -CS, TrDepth, k)
                sc.blit(bg, (0, -150))
                RestoreMyUniverse(k, TrDepth, MainArray)

            if i.key == pygame.K_EQUALS:
                DIV *= 0.9

            if i.key == pygame.K_MINUS:
                DIV *= 1.11111

            if i.key == pygame.K_TAB:
               # sound1.play()
                if Inf:
                    Inf = False
                else:
                    Inf = True

            if i.key == pygame.K_c:
                if m:
                    m = False
                else:
                    m = True

            if i.key == pygame.K_s:
                if SIZE:
                    SIZE = False
                else:
                    SIZE = True

            if i.key == pygame.K_q:
                t *= 1.06

            if i.key == pygame.K_w:
                t *= (50 / 53)

            if i.key == pygame.K_e:
                t += 0.05

            if i.key == pygame.K_r:
                t -= 0.05

            if i.key == pygame.K_y:
                MainArray[ColorR % k].m *= 1.06 

            if i.key == pygame.K_u:
                MainArray[ColorR % k].m *= (50 / 53)

            if i.key == pygame.K_p:
                ColorR += 1

    clock.tick(40)
pygame.quit()