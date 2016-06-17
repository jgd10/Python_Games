"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""
 
import pygame
import math
import random

def update_wind(vx,vy):
    wind_speed_x = vx
    wind_speed_y = vy
    x0,y0 = 50,50
    radius = 2**5
    theta = math.atan2(vy,vx)#(vy/max(vx,1.e-9))
    x1 = radius*math.cos(theta) + x0
    y1 = -radius*math.sin(theta) + y0
    pygame.draw.circle(screen, WHITE, [x0, y0], radius)
    pygame.draw.aaline(screen, RED, [x0, y0],[x1, y1], 5)
    return

def wind_lines(vx,vy,x0,y0):
    theta = math.atan2(vy,vx)
    radius = 2**7
    x1 = int(radius*math.cos(theta)) + x0
    y1 = int(-radius*math.sin(theta)) + y0
    mag = int(math.sqrt(vx**2. + vy**2.))/5
    pygame.draw.line(screen,WHITE,[x0,y0],[x1,y1],mag)
    return

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
SEA_BLUE = (10,105,148)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (2**10, 2**9)
WIDTH = 2**10
HEIGHT = 2**9
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Sail Away")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

x0 = int(random.random()*WIDTH)
y0 = int(random.random()*HEIGHT)
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    vx,vy = 0,-50
    update_wind(vx,vy)
    wind_lines(vx,vy,x0,y0)
    if pygame.time.get_ticks() % 12 == 0:
        x0 = int(random.random()*WIDTH)
        y0 = int(random.random()*HEIGHT)
    # --- Game logic should go here
 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
 
    # --- Drawing code should go here
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    screen.fill(SEA_BLUE)
    clock.tick(60)
 
# Close the window and quit.
pygame.quit()
