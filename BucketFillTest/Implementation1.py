import pygame, random, easygui, sys, os
from pygame.locals import *


class Solution1():
    
    """
    I have implemented this by placing a color palette on the 'pygame screen', where users can pick any color from palette and 
    paint them on the screen. I think 'screen.get_at' method helped me a lot. It was simple and really cool. 
    I have loaded an image which is like a palette and transformed it, to fix it properly. I had to use 'blit method' for displaying the image. 
    I tracked the position using 'e.pos'.
    """
    global screen
    
    #initialization, 'screen' is the one which creates the pygame display canvas.
    
    screen = pygame.display.set_mode((800,600))
    draw_on = False
    last_pos = (0, 0)
    global radius
    radius = 10
    drawColor = (0,0,0)
    screen.fill((255,255,255))
    banner = pygame.image.load("spectrum.jpg")
    banner = pygame.transform.scale(banner, (320, 320))
    screen.blit(banner,(0,0))

    #passing parameters for drawing a cricle
    def fill(x, y, color):
        dx = y[0]-x[0]
        dy = y[1]-x[1]
        distance = max(abs(dx), abs(dy))
        for i in range(distance):
            start = int( x[0]+float(i)/distance*dx)
            end = int( x[1]+float(i)/distance*dy)
            pygame.draw.circle(screen, color, (start, end), radius)

    #This loop saves the image, extracts the color from the pallete on the screen, & does some interactive stuff!! 
    try:
        while True:
            e = pygame.event.wait()
            if e.type == pygame.QUIT:
                extensionchoice = easygui.enterbox("Which file extension would you like to use?")
                if extensionchoice == ".png":
                    extension = ".png"
                elif extensionchoice == ".jpg":
                    extension = ".jpg"
                elif extensionchoice == ".jpeg":
                    extension = ".jpeg"
                savelocation = easygui.filesavebox()
                if savelocation == None:
                    pass
                else:
                    savelocation = os.path.splitext(savelocation)[0]
                    pygame.image.save(screen, savelocation + extension)
                    imagename = savelocation + extension
                    #pygame.display.set_caption("PixelPaint - " + store.imagename)
                    #self.saved = True
                raise StopIteration
            if e.type == pygame.KEYDOWN:
                if e.key == K_ESCAPE:
                    extensionchoice = easygui.enterbox("Which file extension would you like to use?")
                    if extensionchoice == ".png":
                        extension = ".png"
                    elif extensionchoice == ".jpg":
                        extension = ".jpg"
                    elif extensionchoice == ".jpeg":
                        extension = ".jpeg"
                    savelocation = easygui.filesavebox()
                    if savelocation == None:
                        pass
                    else:
                        savelocation = os.path.splitext(savelocation)[0]
                        pygame.image.save(screen, savelocation + extension)
                        imagename = savelocation + extension
                    #pygame.display.set_caption("PixelPaint - " + store.imagename)
                    #self.saved = True
                    raise StopIteration
            if e.type == pygame.MOUSEBUTTONDOWN:
                if e.pos[0]>=320:
                    pygame.draw.circle(screen, drawColor, e.pos, radius)
                    draw_on = True
                else:
                    if e.pos[1]<320:
                        drawColor = screen.get_at(e.pos)
            if e.type == pygame.MOUSEBUTTONUP:
                draw_on = False
            if e.type == pygame.MOUSEMOTION:
                if e.pos[0]>=320:
                    if draw_on:
                        pygame.draw.circle(screen, drawColor, e.pos, radius)
                        fill(e.pos, last_pos, drawColor)
                    last_pos = e.pos
            pygame.display.flip()

    except StopIteration:
        pass        
    pygame.quit()
