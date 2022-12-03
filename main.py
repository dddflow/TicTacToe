import pygame
import sys
from pygame.color import THECOLORS

pygame.init()

screen = pygame.display.set_mode((400, 400))
screen.fill(THECOLORS['azure4'])
pygame.display.set_caption("tic-tac-toe")

pygame.draw.line(screen, THECOLORS['black'], (150, 50), (150, 350), 5)
pygame.draw.line(screen, THECOLORS['black'], (250, 50), (250, 350), 5)
pygame.draw.line(screen, THECOLORS['black'], (50, 150), (350, 150), 5)
pygame.draw.line(screen, THECOLORS['black'], (50, 250), (350, 250), 5)

parts = [pygame.Rect(53, 53, 95, 95), pygame.Rect(153, 53, 95, 95), pygame.Rect(253, 53, 95, 95),
         pygame.Rect(53, 153, 95, 95), pygame.Rect(153, 153, 95, 95), pygame.Rect(253, 153, 95, 95),
         pygame.Rect(53, 253, 95, 95), pygame.Rect(153, 253, 95, 95), pygame.Rect(253, 253, 95, 95)]
areas = [[50, 150, 50, 150], [150, 250, 50, 150], [250, 350, 50, 150],
         [50, 150, 150, 250], [150, 250, 150, 250], [250, 350, 150, 250],
         [50, 150, 250, 350], [150, 250, 250, 350], [250, 350, 250, 350]]

dr = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            dr = True
        pygame.display.flip()

    mouse = pygame.mouse.get_pos()
    for i in range(9):
        if areas[i][0] < mouse[0] < areas[i][1] and areas[i][2] < mouse[1] < areas[i][3]:
            pygame.draw.rect(screen, THECOLORS['azure3'], parts[i])
        else:
            pygame.draw.rect(screen, THECOLORS['azure4'], parts[i])
    # if dr:
    # pygame.draw.circle(screen, THECOLORS['firebrick1'], (100, 100), 40, 4)




