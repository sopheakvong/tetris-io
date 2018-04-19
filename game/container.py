import pygame
from globalvars import *

class Container:
    def __init__(self):
        self.width = BLOCK_SIZE*CONTAINER_WIDTH
        self.height = BLOCK_SIZE*CONTAINER_HEIGHT
        self.xPos = int(round((W/2)-(self.width/2),0))
        self.yPos = int(H-self.height-(BLOCK_SIZE*2))
        self.bordercolor = GRAY
        self.borderRects = []

        # create a list of rects that will make up the border
        for i in range(0,self.width,BLOCK_SIZE):
            for j in range(0,self.height,BLOCK_SIZE):
                if i in [0,self.width-BLOCK_SIZE] or j in [0,self.height-BLOCK_SIZE]:
                    self.borderRects.append(pygame.Rect(self.xPos+i ,self.yPos+j, BLOCK_SIZE, BLOCK_SIZE))


    def draw(self, screen):
        # draw border
        for rect in self.borderRects:
            pygame.draw.rect(screen, self.bordercolor, rect)
            pygame.draw.rect(screen, SHADOW, rect, 2)