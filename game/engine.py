import pygame
from .container import Container
from .block import Block
from globalvars import *

class Engine():
    def __init__(self, screen, Container):
        self.container = Container


    def draw(self, screen):
        self.container.draw(screen)