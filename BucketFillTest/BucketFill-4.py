"""
Bucket Fill Exercise

Imagine you are working on an image editing application. You need to implement a bucket fill tool similar to the one
in paint. The user will use the tool by selecting a color and clicking on the canvas. The tool fills the selected
region of color with the new color.

When a pixel is filled, all of its neighbors (above, below, left, or right) of the same color must also be filled,
as well as their neighbors, and so on, until the entire region has been filled with the new color.

In this exercise, you must write *TWO* implementations of the tool. Each implementation must be different. It is not
required that you invent the solutions yourself. You are encouraged to research the problem. Please write documentation
explaining the difference of each implementation, such as when one solution might be more appropriate than the other.
Don't forget to validate input. There is one existing test, however, you might consider adding some more. Keep in mind
that although the given canvas is small, the solution should be applicable for a real canvas that could have huge
resolutions.

Please use python3 to complete this assignment.
"""
import pygame, os, easygui, sys, random
from pygame.locals import *

class Canvas(object):
    def __init__(self, pixels):
        self.pixels = pixels

    def __str__(self):
        return '\n'.join(map(lambda row: ''.join(row), self.pixels))

    def fill(self, x, y, color):
        """
        Fills a region of color at a given location with a given color.

        :param x:  the x coordinate where the user clicked
        :param y: the y coordinate where the user clicked
        :param color: the specified color to change the region to
        """
        raise NotImplementedError  # Override this function in the Solution classes


class Solution1(Canvas):
    
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
    

class Solution2(Canvas):
    
    """
    This is plain with white background palette. I have implemented this using keys. 
    There is nothing on screen, completely blank white. 
    On welcomeScreen all the instructions are displayed, anytime user can hit key "p" to 
    see the instructions back. Users can change colors by hitting keys. 
    On homeScreen users can see all the instructions. Users can quit or save file or fill colors!!
    """
    
    # TODO write documentation
    #initialization
    pygame.init()
    screen=pygame.display.set_mode((640,480))
    #init and display.set_mode takes care of pygame canvas
    pygame.display.set_caption('Let\'s Paint')
    startPos = (0,0)
    endPos = (0,0)
    color = (0,0,0)
    #The fill mothod basically has everything of this call from background screen, clocktime, font, color, etc.,
    def fill(x, y, color):
        welcomeScreen = True
        background=pygame.Surface(screen.get_size())
        background=background.convert()
        clock=pygame.time.Clock()
        background.fill((255,255,255))
        font=pygame.font.SysFont('arial',20)
        colorName="Black"
        welcomeFont=pygame.font.SysFont('arial',30)
        colorConfigFont=pygame.font.SysFont('arial',20)

        while 1:
        #welcomescreen
           while welcomeScreen:
             for i in pygame.event.get():
                mainScreenPressed=pygame.key.get_pressed()
                if i.type==QUIT or mainScreenPressed[K_q]:
                     exit()
                screen.fill((0,0,0))
                screen.blit(welcomeFont.render("Paint Program Example For Learning",True,(0,255,0)),(100,100))
                screen.blit(colorConfigFont.render("Painting Options",True,(0,255,0)),(100,150))
                screen.blit(colorConfigFont.render("d-Default Color(Black)",True,(0,255,0)),(100,175))
                screen.blit(colorConfigFont.render("b-Blue Color",True,(0,255,0)),(100,200))
                screen.blit(colorConfigFont.render("r-Red Color",True,(0,255,0)),(100,225))
                screen.blit(colorConfigFont.render("y-Yellow Color",True,(0,255,0)),(100,250))
                screen.blit(colorConfigFont.render("g-Green Color",True,(0,255,0)),(100,275))
                screen.blit(colorConfigFont.render("e-Eraser",True,(0,255,0)),(100,300))
                screen.blit(colorConfigFont.render("s-Save Image",True,(0,255,0)),(100,325))
                screen.blit(colorConfigFont.render("l-Load Image",True,(0,255,0)),(100,350))
                screen.blit(welcomeFont.render("Press p for painting",True,(0,255,0)),(100,400))
                pygame.display.flip()
                if mainScreenPressed[K_p]:
                    welcomeScreen=False

       #paint screen, remember only keys for picking any colors :)        
           pressed=pygame.key.get_pressed()
           if pressed[K_r]:
              color=(255,0,0)
              colorName="Red"
           elif pressed[K_g]:
              color=(0,255,0)
              colorName="Green"
           elif pressed[K_b]:
              color=(0,0,255)
              colorName="Blue"
           elif pressed[K_y]:
              color=(255,255,0)
              colorName="Yellow"
           elif pressed[K_e]:
              color=(255,255,255)
              colorNAme="White"
           elif pressed[K_d]:
              color=(0,0,0)
              colorName="Black"
           elif pressed[K_c]:
              color=(0,0,0)
              colorName="Black"
              welcomeScreen=True
           elif pressed[K_s]:
              pygame.image.save(background,'image.png')
           elif pressed[K_l]:
              background=pygame.image.load('image.png')
              colorName="Black"
              color=(0,0,0)

           #this gets me the position and detects the events like mousemotions.
           for i in pygame.event.get():
               if i.type==QUIT or pressed[K_q]:
                   exit()
               elif i.type==pygame.MOUSEMOTION:
                   endPos=pygame.mouse.get_pos()
                   if pygame.mouse.get_pressed()==(1,0,0):
                       pygame.draw.line(background,color,startPos,endPos,10)
                   startPos=endPos
   
           screen.blit(background,(0,0))
           if color==(255,255,255):
               screen.blit(font.render("Eraser In Use",True,(0,0,0)),(400,400))
               screen.blit(font.render("Press c for painting options",True,(0,0,0)),(100,400))
           else:
               screen.blit(font.render("Press c for painting options",True,(0,0,0)),(100,400))   
               screen.blit(font.render("Color In Use : %s"%colorName,True,color),(400,400))
           pygame.display.flip()
       
           if __name__ == '__main__':
               fill(self, startPos, endPos, color)



def test_solution(impl):
    s = impl([
        ['O', 'X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'O', '#', 'O', 'X'],
        ['X', 'O', 'O', 'O', 'X'],
        ['X', 'X', 'X', 'X', 'X'],
        ['X', 'X', 'X', '#', '#'],
        ['X', 'X', 'X', 'X', 'X']
    ])
    s.fill(0, 1, '*')
    s.fill(5, 4, 'O')
    s.fill(2, 2, '@')
    assert str(s) == 'O****\n*OOO*\n*O@O*\n*OOO*\n*****\n***OO\n*****'


if __name__ == '__main__':
    test_solution(Solution1)
    test_solution(Solution2)
    
