# Imports 'numpy' which is a python package containing mathematical functions
import numpy as np

# Imports specifically 'tello' package which is the drone used in this project
from djitellopy import tello

# GUI and manual control import
import pygame as pg

from time import sleep

drone = tello.Tello()


# Variables involving camera size, PID controller and PID Error
width, height = 360, 240
controller = [0.2, 0.2, 0]
error1 = 0

# Initilise pygame allowing for controls to work
pg.init()

# Function which hanldes the getting the user keyboard inputs
def keyPress(key):

    press = False
    for i in pg.event.get(): pass
    myKey = getattr(pg, 'K_{}'.format(key))

    if pg.key.get_pressed()[myKey]:
        press = True
    pg.display.update()
    return press



# Commands controlling visual attributes
black = (0, 0, 0)
screen = pg.display.set_mode((400, 250))
pg.display.set_caption('Controls')
font = pg.font.Font('freesansbold.ttf', 31)

# Commands controlling the text to be displayed
text = font.render('Manual Controls', True, black)
text2 = font.render('W-A-S-D' , True, black)
text3 = font.render('UP & Down Arrow Keys' , True, black)

# Creating a surface for each of the text
displayTxt = text.get_rect()
displayTxt2 = text2.get_rect()
displayTxt3 = text3.get_rect()

# Position of the text
displayTxt.center = (200, 50 )
displayTxt2.center = (200, 100)
displayTxt3.center = (200, 120)

# Background image
background_image = pg.image.load('background/background.png')
screen.blit(background_image, (0, 0))

# Display the text
screen.blit(text, displayTxt)
screen.blit(text2, displayTxt2)
screen.blit(text3, displayTxt3)

# Brings all the previous pygame visual attributes and runs them
for i in pg.event.get():
    pg.display.update()


# Keyboard inputs and their movement for the drone
def buttonPress():
    forwardBackward, upDown, leftRight = 0, 0, 0

    if keyPress("w"):
        forwardBackward = 50
    elif keyPress("s"):
        forwardBackward = -50

    if keyPress("UP"):
        upDown = 50
    elif keyPress("DOWN"):
        upDown = -50

    if keyPress("a"):
        leftRight = -50
    elif keyPress("d"):
        leftRight = 50
        
    if keyPress("l"):
        drone.land()
        drone.streamoff()
        pg.quit()
        sleep(2)
        
    return [forwardBackward, upDown, leftRight]

# Autonomous face tracking movement function
def tracking(data, width, controller, error1):

    axis, axis2 = data[0]
    forward_backward = 0

    # Controls the drone tracking when the user moves left or right
    move = controller[0] * (axis - width // 2) + \
           controller[1] * (axis - width // 2)


    # The specifc rotation the drone will have to do
    rotate = int(np.clip((move - error1), -95,95))

    try:
    # Handles drone moving back and forward depending
    # on how large the user is within the camera
        if data[1] > 6300 and data[1] < 6900:
            forward_backward = 0
        elif data[1] > 6800:
            forward_backward= -15
        elif data[1] < 6200 and data[1] !=0:
            forward_backward=15

        # The drone will not move if the user is
        # neither small nor large within the camera
        elif axis == 0:
            rotate = 0
        elif axis2 == 0:
            rotate = 0


    #Handles any error
    except RuntimeError:
        print("Error detecting faces")


    # Sends the commands to the drone
    move = buttonPress()

    # Conditional statement handling whether the drone moves from the keyboard
    # or from the face tracking

    # manual movement
    if move != [0, 0, 0]:
        drone.send_rc_control(0, move[0], move[1], move[2])
        sleep(0.05)
    
    # autonomous movement
    elif move == [0, 0, 0]:
        drone.send_rc_control(0, forward_backward, 0, rotate)
        return axis - width // 2
        


           

    

