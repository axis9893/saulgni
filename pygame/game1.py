import pygame
import sys
import time
import random

from pygame.locals import *

WINDOW_WIDTH = 800 #가로 크기
WINDOW_HEIGTH = 600 #세로 크기

WHITE = (255, 255, 255)

if __name__ == '__main__':
    pygame.init()
    window = pygame.display.set_mode ((WINDOW_WIDTH, WINDOW_HEIGTH))
    pygame.display.set_caption('Python Game')
    surface = pygame.Surface(window.get_size())
    surface = surface.convert()
    surface.fill(WHITE)
    clock = pygame.time.Clock()
    pygame.key_set_repeat(1, 40)
    window.blit(surface, (0, 0))



