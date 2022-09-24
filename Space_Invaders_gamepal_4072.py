import pygame
import turtle
import random
import math
import os
import sys
import time
import pygame.mixer
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Space Invaders: GAMEPAL EDIITION V0.0X')
pygame.mouse.set_visible(0)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((0, 0, 0))
clock = pygame.time.Clock()
class Invader(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        ## load files from spaceinvaders.py directory
      ## load any file name invader.png
        ## load any file named invader.gif
        self.load = pygame.image.load(os.path.join('https://cdn.discordapp.com/attachments/989290169758789682/1023368548829118494/EYE_PATCH_SUSIE_80x80_spaceship_metallix_retro_atari_rectange_1_40d6a2f0-160b-4c60-b788-e305a3ffb913.png')).convert()
        screen = pygame.display.get_surface()
        self.rect = self.image.get_rect()
        self.reset()
        self.dx = 5
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.left > screen.get_width():
            self.reset()
    def reset(self):
        self.rect.left = 0
        self.rect.centery = random.randrange(0, screen.get_height())
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = pygame.image.load('textures/player.png'), -1
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
    def update(self):
        mousex, mousey = pygame.mouse.get_pos()
        self.rect.center = (40, mousey)
    def reset(self):
        self.rect.left = 0
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = pygame.image.load("https://cdn.discordapp.com/attachments/989290169758789682/1023377275623837726/EYE_PATCH_SUSIE_256x256_-_SCP_4072_Settting_Very_low_-_player_s_4eac8bdc-1cc5-4260-b3ca-b4319a640449.png").convert()
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right > screen.get_width():
            self.reset()
    def reset(self):
        self.rect.left = 0
        self.rect.centery = random.randrange(0, screen.get_height())
        self.dx = 5
class Explosion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = ('https://cdn.discordapp.com/attachments/989290169758789682/1023371854586597476/EYE_PATCH_SUSIE_firecracker_169_SCP_4072_-_Very_low_-_1_ae186eb3-e13a-4c57-91f8-6a551ef58f80.png', -1)
        self.image = self.image.convert()
        self.rect = self.image.get_rect()
        self.reset()
    def update(self):
        self.rect.centerx += self.dx
        if self.rect.right > screen.get_width():
            self.reset()
    def reset(self):
        self.rect.left = 0
        self.rect.centery = random.randrange(0, screen.get_height())
        self.dx = 5
def main():
    screen = pygame.display.set_mode((640, 480))
    pygame.display.set_caption('Space Invaders')
    pygame.mouse.set_visible(0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((0, 0, 0))
    clock = pygame.time.Clock()
    invader1 = Invader()
    player = Player()
    bullet = Bullet()
    explosion = Explosion()
    allSprites = pygame.sprite.OrderedUpdates(invader1, player, bullet, explosion)
    keepGoing = True
    while keepGoing:
        clock.tick(30)
        pygame.mouse.set_visible(0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keepGoing = False
        allSprites.clear(screen, background)
        allSprites.update()
        allSprites.draw(screen)
        pygame.display.flip()
    pygame.quit()
if __name__ == "__main__":
    main()
