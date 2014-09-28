import pygame
import math
pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0,0,255)

PI = 3.141592653

done = False
clock = pygame.time.Clock()

size = (700,500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Mr Duguid's Cool Game")
screen.fill(WHITE)
pygame.display.flip()

width = 0

while not done:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print("Key Pressed")
            width = width +1

    screen.fill(WHITE)
    pygame.draw.line(screen, GREEN, [0,0], [100,100],width)
    y_offset = 0
    while y_offset < 100:
        pygame.draw.line(screen,RED,[0,10+y_offset],[100,110+y_offset],5)
        y_offset = y_offset + 10

    for i in range(200):

        radians_x = i / 20
        radians_y = i / 6

        x = int(75 * math.sin(radians_x)) + 200
        y = int(75 * math.cos(radians_y)) + 200

        pygame.draw.line(screen, BLACK, [x,y], [x+5,y], 5)

    pygame.draw.rect(screen,BLACK,[20,20,250,100],2)
    pygame.draw.ellipse(screen, BLACK, [20,20,250,100], 2)

    pygame.draw.arc(screen, GREEN, [100,100,250,200],PI/2, PI, 2)
    pygame.draw.arc(screen, BLACK, [100,100,250,200],0, PI/2, 2)
    pygame.draw.arc(screen, RED, [100,100,250,200],2*PI/2, 2*PI, 2)
    pygame.draw.arc(screen, BLUE, [100,100,250,200],PI, 3*PI/2, 2)

    pygame.draw.polygon(screen, BLACK, [[200,350], [0,400], [200,450], [400,400]],5)

    font = pygame.font.SysFont('Calibri',25,True,False)

    text = font.render("Some Text",True,GREEN)
    screen.blit(text, [500,250])
    
    pygame.display.flip()

    clock.tick(60)



print("Got Here")
pygame.quit()
