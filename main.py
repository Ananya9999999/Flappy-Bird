import random
import sys
import pygame
from pygame.locals import *

#global variables for game
window_width= 600
window_height= 499

#set height and width of window
window= pygame.display.set_mode((window_width, window_height))
elevation= window_height*0.8
game_images= {}
framespersecond= 32
pipeimage= 'images/pipe.png'
background_image= 'images/background.png'
birdplayer_image= 'images/bird.png'
sealevel_image= 'images/base.jfif'

#program where the game starts
if __name__ == "__main__":

    #initializing modules of pygame library
    pygame.init()
    framespersecond_clock= pygame.time.clock()

    #set the title on top of game window
    pygame.display.set_caption('Flappy Bird Game')

    #load all images
    game_images['scoreimages']= (
        pygame.image.load('images/0.png').convert_alpha(),
        pygame.image.load('images/1.png').convert_alpha(),
        pygame.image.load('images/2.png').convert_alpha(),
        pygame.image.load('images/3.png').convert_alpha(),
        pygame.image.load('images/4.png').convert_alpha(),
        pygame.image.load('images/5.png').convert_alpha(),
        pygame.image.load('images/6.png').convert_alpha(),
        pygame.image.load('images/7.png').convert_alpha(),
        pygame.image.load('images/8.png').convert_alpha(),
        pygame.image.load('images/9.png').convert_alpha(),
    )
    game_images['flappybird']= pygame.image.load(birdplayer_image).convert_alpha()
    game_images['sealevel']= pygame.image.load(sealevel_image).convert_alpha()
    game_images['background']= pygame.image.load(background_image).convert()
    game_images['pipeimage']= (
        pygame.transform.rotate(pygame.image.load(pipeimage).convert_alpha(), 180),
        pygame.image.load(pipeimage).convert_alpha()
    )
    print("WELCOME TO THE FLAPPY BIRD GAME")
    print("Press space bar or enter to start the game")