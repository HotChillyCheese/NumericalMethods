import sys

from graphics import *
Radius = 0.5
Cx = 0.0 #0.7454294
Cy = 0.0
Side = 0.8 #1.7 
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
    Incx = - Side + 2 * Side/M*q#-Side + 2*Side/M*q
    Incy= - Side + 2 *Side/ M*p #- Side + 2*Side/M*p
    x = Incx
    y = Incy
    w=0
    for n in range(1,Num):
        xx = 5*x/6.0 - x*(x*x*x*x - 10*x*x*y*y +5*y*y*y*y)/(x*x+y*y)/(x*x+y*y)/(x*x+y*y)/(x*x+y*y)/(x*x+y*y)/6.0
        yy = 5*y/6.0 + y*(5*x*x*x*x - 10*x*x*y*y + y*y*y*y)/(x*x+y*y)/(x*x+y*y)/(x*x+y*y)/(x*x+y*y)/(x*x+y*y)/6.0
        x = xx
        y = yy
        if (x-Cx)*(x-Cx) + (y-Cy)*(y-Cy) > Radius:
            w = n/N
            rectCol(int(M/3+q),int(M/3+p),int(w))
            break
win.getMouse()
win.close()
