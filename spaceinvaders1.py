"""
Space invaders game for students to update 10/11/2017
"""

import pygame
import random


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400


class Craft(pygame.sprite.Sprite):
    """
    This class represents the enemy craft.
    """

    def __init__(self, colour, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.width = width
        self.rect = self.image.get_rect()
        self.start_x = self.rect.x
        self.move_speed = 1
        self.outOf = False

    def update(self):
        """Call each frame to move across screen"""
        self.rect.x += self.move_speed
        if self.rect.x > SCREEN_WIDTH - self.width or self.rect.x < 1:
            self.move_speed = -self.move_speed
        

class UFO(Craft):
    def __init__(self, colour, width, height):
        Craft.__init__(self, colour, width, height)

        self.move_speed = 2
    
    def update(self):
        self.rect.x += self.move_speed
        if self.rect.x > SCREEN_WIDTH - self.width or self.rect.x < 1:
            self.outOf = True

    def change_direction(self, left=True):
        if left:
            self.move_speed = -self.move_speed


class Laser(pygame.sprite.Sprite):
    """Lasers to shoot"""

    def __init__(self, colour, up=True):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.Surface([4, 8])
        self.image.fill(colour)
        self.width = 4
        self.rect = self.image.get_rect()
        self.start_x = self.rect.x
        if up:
            self.move_speed = -2
        else:
            self.move_speed = 2

    def update(self):
        """Call each frame to move across screen"""
        self.rect.y += self.move_speed


class PlayerCraft(pygame.sprite.Sprite):
    """
    This class represents the players craft.
    """
    
    def __init__(self, colour, width, height):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill(colour)
        self.width = width
        self.height = height
        self.rect = self.image.get_rect()
        self.start_x = self.rect.x
        self.move_speed = 1

    def move(self, right=True):
        if right:
            if self.rect.x < SCREEN_WIDTH - self.width:
                self.rect.x += 2
        else:
            if self.rect.x > 0:
                self.rect.x -= 2

pygame.init()


def main():

    screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

    craft_list = pygame.sprite.Group()

    all_sprites_list = pygame.sprite.Group()

    lives = 5

    place_x = 40
    place_y = 20
    while place_y < 250:
        while place_x < SCREEN_WIDTH - 40:
            craft = Craft(BLUE, 20, 15)
            craft.rect.x = place_x
            craft.rect.y = place_y
            place_x += 40
            craft_list.add(craft)
            all_sprites_list.add(craft)
        place_y += 40
        place_x = 40

    laser_list = pygame.sprite.Group()
    bad_laser_list = pygame.sprite.Group()
    ufo_sprites_list = pygame.sprite.Group()

    player = PlayerCraft(RED, 20, 15)
    player.rect.x = 20
    player.rect.y = SCREEN_HEIGHT - 50
    all_sprites_list.add(player)

    clock = pygame.time.Clock()

    done = False
    while not done:

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(False)
        elif keys[pygame.K_RIGHT]:
            player.move(True)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if len(laser_list.sprites()) < 3:
                        laser = Laser(GREEN)
                        laser.rect.x = player.rect.x + player.width/2 - 2
                        laser.rect.y = player.rect.y - player.height/2
                        all_sprites_list.add(laser)
                        laser_list.add(laser)

        for lzr in laser_list:
            lzr.update()
            block_hit_list = pygame.sprite.spritecollide(lzr, craft_list, True)
            for block in block_hit_list:
                laser_list.remove(lzr)
                all_sprites_list.remove(lzr)
                print(block)
            if lzr.rect.y > SCREEN_HEIGHT or lzr.rect.y < 0:
                laser_list.remove(lzr)
                all_sprites_list.remove(lzr)

        for lzr in bad_laser_list:
            lzr.update()
            if lzr.rect.y > SCREEN_HEIGHT:
                laser_list.remove(lzr)
                all_sprites_list.remove(lzr)

        player_hit_list = pygame.sprite.spritecollide(player, bad_laser_list, True)

        for col in player_hit_list:
            lives -= 1
            print("Lives: ", lives)
            print(col)

        screen.fill(BLACK)

        at_edge = False

        for cft in craft_list:
            cft.update()
            if cft.rect.x < 10 or cft.rect.x > SCREEN_WIDTH - 40:
                at_edge = True
            if random.randint(0, 750) == 0:
                laser = Laser(WHITE, False)
                laser.rect.x = cft.rect.x + cft.width/2 - 2
                laser.rect.y = cft.rect.y + 20
                all_sprites_list.add(laser)
                bad_laser_list.add(laser)

        if at_edge:
            for cft in craft_list:
                cft.move_speed = -cft.move_speed
                cft.rect.y = cft.rect.y + 3

        if random.randint(0, 750) == 0 and len(ufo_sprites_list.sprites()) < 1:
            a_ufo = UFO(WHITE, 30, 10)
            a_ufo.rect.y = 10
            if random.randint(0, 2) == 0:
                a_ufo.rect.x = 30
            else:
                a_ufo.rect.x = SCREEN_WIDTH - 30
                a_ufo.change_direction(True)

            all_sprites_list.add(a_ufo)
            ufo_sprites_list.add(a_ufo)

        if len(ufo_sprites_list.sprites()) > 0:
            for u in ufo_sprites_list:
                u.update()
                if u.outOf:
                    all_sprites_list.remove(a_ufo)
                    ufo_sprites_list.remove(a_ufo)

        all_sprites_list.draw(screen)

        clock.tick(30)

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
