import pygame
import math
pygame.init()

WHITE = (255, 255, 255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

clock = pygame.time.Clock()

size = (500,700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("A Drawing")
screen.fill(WHITE)
pygame.display.flip()

done = False

while not done:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, BLACK, [100,300,200,100])
    pygame.draw.rect(screen, BLUE, [185,350, 30, 50])
    pygame.draw.rect(screen, BLACK, [205, 375, 5, 5])
    pygame.draw.rect(screen, GREEN, [130, 315, 25,30])
    pygame.draw.line(screen, BLACK, (142, 315), (142, 345), 2)
    pygame.draw.line(screen, BLACK, (130, 329), (155, 329), 2)
    pygame.draw.rect(screen, GREEN, [245, 315, 25,30])
    pygame.draw.line(screen, BLACK, (257, 315), (257, 345), 2)
    pygame.draw.line(screen, BLACK, (245, 329), (270, 329), 2)
    pygame.draw.polygon(screen, RED, [[95,301],[200,250],[305,301]])
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
print("Complete!")
