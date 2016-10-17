from pygame import *
from collections import deque 
from sets import Set 
def flood(x,y,newClr,oldClr):
    visit_queue = deque ( [(x,y)] )
    neighbourhood = [ (-1,0), (+1,0), (0,-1), (0,+1) ]
    visited = Set()
    a=0
    pt = []
    while visit_queue:
        for i in range(len(visit_queue)):
            pt.append(visit_queue.popleft())
        for i in range(len(pt)):
            if screen.get_at(pt[i]) != oldClr and pt[i] not in visited:
                screen.set_at(pt[i], newClr)
                visited.add(pt[i])
            for n in neighbourhood: 
                visit_queue.append ( ( pt[i][0] + n[0], pt[i][1] + n[1] ) )
                a+=1
                print a
screen = display.set_mode((1024,768))   #screen is a surface
running = True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running = False
        draw.circle(screen,(0,255,0),(200,100),10,1)
        flood(200,100,(255,0,0),(0,0,0))
    display.flip()
display.flip()
quit()