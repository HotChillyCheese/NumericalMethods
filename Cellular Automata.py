import sys

from graphics import *
Radius = 30
Cx = 0.5 #0.7454294
Cy = 0.0
Side = 1.3 #1.7 
M = 300
N = 1
Num = 256*N
sT=5
w = 0
# x = 0.0
# y = 0.0

import random
p = M/2+random.randrange(-M/2,M/2)
q = M/2+random.randrange(-M/2,M/2)

win = GraphWin("Mandelbrot", int(5*M/3),int(5*M/3))


def rectCol(p,q,w):
    Rect = Rectangle(Point(int(p-sT/2),int(q-sT/2)), 
    Point(int(p+sT/2),int(q+sT/2))) 
    Rect.draw(win).setFill(color_rgb(int(10*w%255), 
    int((128-10*w)%255),int((128+10*w)%255)))

i = 1
while i > 0:
    p = p+random.randrange(-1,2)*sT
    q = q+random.randrange(-1,2)*sT
    if p < 0:
        p = p+2
    elif p > M:
        p = p-2
    
    if q < 0:
        q = q+2
    elif q > M:
        q = q-2
    Incx = Cx - Side + 2 * Side/M*q#-Side + 2*Side/M*q
    Incy= Cy - Side + 2 *Side/ M*p #- Side + 2*Side/M*p
    x = 0.0#Incx
    y = 0.0#Incy
    w=0
    for n in range(1,Num):
        xx = x*x - y*y - Incx# Cx
        yy = 2*x*y - Incy#Cy
        x = xx
        y = yy
        if x*x + y*y > Radius:
            w = n/N
            rectCol(int(M/3+q),int(M/3+p),int(w))
            break
win.getMouse()
win.close()
