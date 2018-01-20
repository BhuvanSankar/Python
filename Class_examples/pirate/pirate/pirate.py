#!/usr/bin/python3

# To run this you need to install pygame - see
# http://www.pygame.org/news.html

import os,sys,pygame,random, math


# Some globals
plank_start = (510, 490)      # the position to start the pirate
plank_end = (320, 563)        # the end of the plank
plank_steps = 5               # how many steps on the plank

plank_dx = (plank_end[0] - plank_start[0])//plank_steps   # delta x for a step
plank_dy = (plank_end[1] - plank_start[1])//plank_steps   # delta y for a step


def load_image(name):
    """ Load image and return image object"""

    fullname = os.path.join('data', name)
    try:
            image = pygame.image.load(fullname)
            if image.get_alpha() is None:
                image = image.convert()
            else:
                image = image.convert_alpha()
    except pygame.error as message:
            print('Cannot load image:', fullname)
            raise SystemExit(message)
    return image

class Pirate(pygame.sprite.Sprite):
    """ The pirate sprite."""

    def __init__(self, counter):
        pygame.sprite.Sprite.__init__(self)
        self.counter = counter
        self.image = load_image("pirate.gif")
        self.rect = self.image.get_rect()
        self.start = plank_start
        self.end = plank_end
        self.dx = plank_dx
        self.dy = plank_dy
        self.rect.bottomright = plank_start
        self.x, self.y = plank_start

    def step(self, coin):
        """The pirate takes a step.

        coin == 0 means a tail is thrown

        """

        if self.x < self.end[0]:
            # pirate has fallen off plank - don't step
            return
        # update step counter
        self.counter.inc()
        if coin == 0:
            # tails
            if (self.x, self.y) != self.start:
                # not at beginning so step back
                self.x -= self.dx
                self.y -= self.dy
        else:
            # head - step forward
            self.x += self.dx
            self.y += self.dy

    def update(self):
        """Define the update method for the Pirate sprite object.

        This determines where the sprite is drawn when the sprites are updated.

        """

        self.rect.bottomright = (self.x, self.y)
        if self.x < self.end[0]:
            # falling
            self.y += 10
        if self.y > 1000:
            # in the drink - re-incarnate pirate
            self.counter.reset()
            pygame.time.delay(1000)
            self.rect.bottomright = self.start
            self.x, self.y = self.start

class Coin(pygame.sprite.Sprite):
    """The coin sprite."""

    def __init__(self, pirate, bottom):
        self.pirate = pirate
        pygame.sprite.Sprite.__init__(self)
        self.head_image = load_image("head.gif")
        self.tail_image = load_image("tail.gif")
        self.rect = self.head_image.get_rect()
        self.images = [self.tail_image, self.head_image]
        self.rect.bottomleft = (10, bottom - 10)
        self.countdown = 0
        self.image = self.head_image
        self.side = 1          # side of coin - 0 = tail, 1 = head
        self.tossing = False   # is the coin being tossed?
	
    def step(self, side):
        # side is the result of the coin toss - start the flipping
        self.side = side
        self.countdown = 30    # timesteps for coil flipping
        self.tossing = True

    def get_top(self):
        return self.rect.top

    def update(self):
        if self.tossing:
            if self.countdown == 0:
                self.tossing = False
                self.pirate.step(self.side)
                return
            elif self.countdown % 5 == 0:
                # every 5 timesteps show other side of coin
                self.side = 1 - self.side
                self.image = self.images[self.side]
            self.countdown -= 1     

class Count(pygame.sprite.Sprite):
    """The counter sprite - shows the number of steps."""

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 50)
        # create a surface big enough to hold 4 digits
        text = self.font.render('9999', True, (255,0,0), (0, 0, 255))
        self.rect = text.get_rect()
        self.image = pygame.Surface((self.rect.width, self.rect.height)).convert()
        self.image.blit(text, self.rect)
        self.right = self.rect.right
        self.reset()

    def set_position(self, top_of_coin):
        self.rect.bottomleft = (10, top_of_coin - 10)

    def update(self):
        self.image.fill((0, 0, 255))
        text = self.font.render("%d" % self.counter, True, (255,0,0), (0, 0, 255))
        textrect = text.get_rect()
        textrect.right = self.right
        self.image.blit(text, textrect)
        
    def reset(self):
        self.counter = 0

    def inc(self):
        self.counter += 1
        
        
if __name__ == '__main__':
    pygame.init()
    size = (900,900) # start off with a big enough size
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Walk the plank')
    ship = load_image("ship.gif")
    rect = ship.get_rect()
    # reset the screen size of the size of the ship image
    screen = pygame.display.set_mode((rect.width, rect.height))
    # draw the ship
    screen.blit(ship, (0,0))
    counter = Count()
    pirate = Pirate(counter)
    coin = Coin(pirate, rect.bottom)
    counter.set_position(coin.get_top())
    # Create a render updates sprite group
    sprites = pygame.sprite.RenderUpdates()
    # add the sprites to the group
    sprites.add(pirate)
    sprites.add(coin)
    sprites.add(counter)
    # render the scene
    pygame.display.update()
    increment = 0
    while True:
        for event in pygame.event.get():
            # exit on the QUIT event
            if event.type == pygame.QUIT: sys.exit()
        sprites.update()
        # determine the rectangles that need updating
        rectlist = sprites.draw(screen)
        # update them (draw them)
        pygame.display.update(rectlist)
        # sleep for 10ms
        pygame.time.delay(10)
        increment += 1
        if increment == 80:
            # after 80 timesteps flip a coin and step
            increment = 0
            toss = random.randint(0,1)
            coin.step(toss)
        # remove the sprites - get ready to redraw
        sprites.clear(screen, ship)
