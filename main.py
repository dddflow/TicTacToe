import pygame
import sys
from pygame.color import THECOLORS


pygame.init()

screen = pygame.display.set_mode((400, 400))
screen.fill(THECOLORS['azure4'])

pygame.draw.line(screen, THECOLORS['black'], (150, 50), (150, 350), 5)
pygame.draw.line(screen, THECOLORS['black'], (250, 50), (250, 350), 5)
pygame.draw.line(screen, THECOLORS['black'], (50, 150), (350, 150), 5)
pygame.draw.line(screen, THECOLORS['black'], (50, 250), (350, 250), 5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        pygame.display.flip()


