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

def flappygame():
    your_score=0
    horizontal= int(window_width/5)
    vertical= int(window_height/2)
    ground=0
    mytempheight=100

    #generating two pipes for blitting on window
    first_pipe= createPipe()
    second_pipe= createPipe()

    #list containing lower pipes
    down_pipes= [
        {'x': window_width+300-mytempheight,
         'y': first_pipe[1]['y']},
        {'x': window_width+300-mytempheight+(window_width/2),
         'y': second_pipe[1]['y']},
    ]

    #list containing upper pipes
    up_pipes= [
        {'x': window_width+300-mytempheight,
         'y': first_pipe[0]['y']},
        {'x': window_width+300-mytempheight+(window_width/2),
         'y': second_pipe[0]['y']}, 
    ]

    pipeVelX= -4 #pipe velocity along x

    bird_velocity_y=-9 #bird velocity
    bird_max_velocity_y= 10
    bird_min_vel_y=-8
    birdaccy=1

    #velocity while flapping
    bird_flap_velocity= -8

    #it is true only when the bird is flapping
    bird_flapped= False
    while True:
        #handling the key pressing events
        for event in pygame.event.get():
            if event.type== QUIT or (event.type== KEYDOWN and event.key== K_ESCAPE):
                pygame.quit()
                sys.exit()

            if event.type== KEYDOWN and (event.key== K_SPACE or event.key== K_UP):
                if vertical > 0:
                    bird_velocity_y= bird_flap_velocity
                    bird_flapped= True
        
        #check for game over
        gameover= isGameOver(horizontal, vertical, up_pipes, down_pipes)
        if gameover:
            return
        
        #check for score
        playerMidPos= horizontal + game_images['flappybird'].get_width()/2
        for pipe in up_pipes:
            pipeMidPos= pipe['x'] + game_images['pipeimage'][0].get_width()/2
            if pipeMidPos <= playerMidPos < pipeMidPos +4:
                your_score+=1
                print(f"Your score is {your_score}")
        
        if bird_velocity_y < bird_max_velocity_y and not bird_flapped:
            bird_velocity_y+= birdaccy
        
        if bird_flapped:
            bird_flapped= False
        playerHeight= game_images['flappybird'].get_height()
        vertical= vertical + min(bird_velocity_y, elevation - vertical - playerHeight)

        #move pipes to left
        for upperpipe, lowerpipe in zip(up_pipes, down_pipes):
            upperpipe['x']+= pipeVelX
            lowerpipe['x']+= pipeVelX
        
        #add a new pipe when the first is about to cross the leftmost part of the screen
        if 0 < up_pipes[0]['x'] < 5:
            newpipe= createPipe()
            up_pipes.append(newpipe[0])
            down_pipes.append(newpipe[1])
        
        #if the pipe is out of the screen, remove it
        if up_pipes[0]['x'] < -game_images['pipeimage'][0].get_width():
            up_pipes.pop(0)
            down_pipes.pop(0)
        
        #blitting all images on the window
        window.blit(game_images['background'], (0, 0))
        for upperpipe, lowerpipe in zip(up_pipes, down_pipes):
            window.blit(game_images['pipeimage'][0], (upperpipe['x'], upperpipe['y']))
            window.blit(game_images['pipeimage'][1], (lowerpipe['x'], lowerpipe['y']))
        window.blit(game_images['sealevel'], (ground, elevation))
        window.blit(game_images['flappybird'], (horizontal, vertical))

        #showing the score on the window
        mydigits= [int(x) for x in str(your_score)]
        width=0

        for digit in mydigits:
            width+= game_images['scoreimages'][digit].get_width()
        Xoffset= (window_width - width)/1.1

        for digit in mydigits:
            window.blit(game_images['scoreimages'][digit], (Xoffset, window_height*0.02))
            Xoffset+= game_images['scoreimages'][digit].get_width()

        #refreshing the game window
        pygame.display.update()

        #set the frame per second
        framespersecond_clock.tick(framespersecond)

#checking if bird is above sealevel
def isGameOver(horizontal, vertical, upperpipes, lowerpipes):
    #if bird touches sealevel
    if vertical > elevation - 25 or vertical < 0:
        return True

    #if bird touches any pipe
    for pipe in upperpipes:
        pipeHeight= game_images['pipeimage'][0].get_height()
        if (vertical < pipeHeight + pipe['y'] and abs(horizontal - pipe['x']) < game_images['pipeimage'][0].get_width()):
            return True

    for pipe in lowerpipes:
        if (vertical + game_images['flappybird'].get_height() > pipe['y']) and abs(horizontal - pipe['x']) < game_images['pipeimage'][0].get_width():
            return True

    return False

def createPipe():
    offset= window_height/3
    pipeHeight= game_images['pipemimage'][0].get_height()

    #generating random pole heights
    y2= offset + random.randrange(0, int(window_height - game_images['sealevel'].get_height() - 1.2 * offset))
    pipeX= window_width + 10
    y1= pipeHeight - y2 + offset
    pipe= [
        #upper pipe
        {'x': pipeX, 'y': -y1},
        #lower pipe
        {'x': pipeX, 'y': y2}
    ]     
    return pipe
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

    #main game starts
    while True:
        #sets the coordinate of flappy bird
        horizontal= int(window_width/5)
        vertical= int((window_height - game_images['flappybird'].get_height())/2)

        #for sealevel
        ground=0
        while True:
            for event in pygame.event.get():

                #if user clicks on cross button, close the game
                if event.type== QUIT or (event.type== KEYDOWN and event.key== K_ESCAPE):
                    pygame.quit()
                    #exit the program
                    sys.exit()

                #if the user presses space or up key, start the game
                elif event.type== KEYDOWN and (event.key== K_SPACE or event.key== K_UP):
                    flappygame()

                #if user doesn't press anykey Nothing happen
                else:
                    window.blit(game_images['background'], (0, 0))
                    window.blit(game_images['flappybird'], (horizontal, vertical))
                    window.blit(game_images['sealevel'], (ground, elevation))

                    #Just refresh the screen
                    pygame.display.update()

                    #set the rate of frame per second
                    framespersecond_clock.tick(framespersecond)

