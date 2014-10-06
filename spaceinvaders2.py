class Craft(pygame.sprite.Sprite):
    """
    This class represents a craft. This could be alien, UFO or player. Requires colour for the colour of the craft
    and the width and height of the craft.
    """

    #This part sets up te craft when it is created.
    def __init__(self, colour, width, height):
        pygame.sprite.Sprite.__init__(self)

        #sets the height and width of the craft as entered
        self.image = pygame.Surface([width, height])
        #fills in the defined colour for the craft
        self.image.fill(colour)

        self.width = width
        # makes the rectangle within which sits the craft
        self.rect = self.image.get_rect()
        #stores the starting point of the craft
        self.startx = self.rect.x
        # Sets the speed at which the craft moves (currently one pixel per loop)
        self.move_speed = 1
        # Used to store if the craft is out of the screen
        self.outOf = False
        

    def update(self):
        """Call each frame to move the craft across screen"""
        #default behavious is for a craft to move accross the screen
        self.rect.x += self.move_speed
        #default behaviour for a craft is to register outOf as true if it goes out of the screen
        if self.rect.x > SCREEN_WIDTH - self.width or self.rect.x < 1 or self.rect.y > SCREEN_HEIGHT or self.rect.y < 0:
            self.outOf = True

