#!/usr/bin/env python

#########
# 2016 Copyright (C) James Derrick
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# ### ABOUT THE GAME ###
#
# NB This is written for python 2.7!
#
# This is a simple recreation of the popular slime volleyball game, which
# can be found here: http://slimegames.eu/ . However, none of the same code
# was used and everything was reverse engineered from the memories of 
# hours of fun I had as a kid! This version is in python.
#
# I also used Simon Mouradian's pong game as a template to build this.
# Simon's game can be found here: https://github.com/slmouradian/pong
# Also on github.
#
# ### HOW TO PLAY ###
# -----------------------------------
# ACTION   | LEFT SLIME | RIGHT SLIME|
# -----------------------------------
# JUMP     |     W      |      I     |
# MV LEFT  |     A      |      J     |
# MV RIGHT |     D      |      L     |
# -----------------------------------
#
# As in tennis you are allowed one bounce of the ball in your 'court' (half)
# after this, if the ball touches the floor of your court, your opponent scores
# a point and vice versa. The net is mainly cosmetic at this stage, and simply
# divides the courts.
#
# Please enjoy! 
#########

from Tkinter import *
import numpy as np
import string
import random
import slimeball_levels as slv


WIDTH = 1100.
HEIGHT = 500.
BALL_RADIUS = 14.
BALL_R = BALL_RADIUS
SLIME_R = 40.
BALL_MASS = 15.
SLIME_MASS = 30.

slv.initialise_levels(WIDTH,HEIGHT,BALL_R,SLIME_R,BALL_MASS,SLIME_MASS)
"""
# Red brick: Largest ball
BRICK_R_r   = 60.
BRICK_R_m   = 600
BRICK_R_COL = 'red'
BRICK_R_hp  = 5.

# Blue brick: Smaller ball
BRICK_B_r   = 50.   
BRICK_B_m   = 400.
BRICK_B_COL = 'blue'
BRICK_B_hp  = 10.

# Magenta brick: Smallest ball. Most HP.
BRICK_M_r   = 40.   
BRICK_M_m   = 200.
BRICK_M_COL = 'magenta'
BRICK_M_hp  = 15.

LEFT = True
RIGHT = False
"""
LINE_COLOUR='black'
BALL_COLOUR='black'
SLIME_COLOUR='black'
slime_acc = 10.

"""
def level_1a():
	global bricks, redbrick1,redbrick2,bricks,bricks_original

	rb1pos    = [WIDTH/2.-BRICK_R_r,         HEIGHT/4.]
	rb2pos    = [WIDTH/2.-BRICK_R_r,      3.*HEIGHT/4.]
	rb2pos    = [3.*WIDTH/4.-2.*BRICK_R_r,   HEIGHT/2.]
	redbrick1 = canvas.create_oval(rb1pos[0]-BRICK_R_r,rb1pos[1]+BRICK_R_r,rb1pos[0]+BRICK_R_r,rb1pos[1]-BRICK_R_r, 
                                          fill=BRICK_R_COL)
	redbrick2 = canvas.create_oval(rb2pos[0]-BRICK_R_r,rb2pos[1]+BRICK_R_r,rb2pos[0]+BRICK_R_r,rb2pos[1]-BRICK_R_r, 
                                          fill=BRICK_R_COL)
	redbrick3 = canvas.create_oval(rb3pos[0]-BRICK_R_r,rb3pos[1]+BRICK_R_r,rb3pos[0]+BRICK_R_r,rb3pos[1]-BRICK_R_r, 
                                          fill=BRICK_R_COL)
	redb1 = {'radius': BRICK_R_r,'mass': BRICK_R_m, 'tag': redbrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_R_hp,
					'color':'red','start_pos': rb1pos}
	redb2 = {'radius': BRICK_R_r,'mass': BRICK_R_m, 'tag': redbrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_R_hp,
					'color':'red','start_pos': rb2pos}
	redb3 = {'radius': BRICK_R_r,'mass': BRICK_R_m, 'tag': redbrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_R_hp,
					'color':'red','start_pos': rb2pos}
	bricks  = [redb1,redb2,redb3]
	bricks_original  = [redb1,redb2,redb3]
"""
def ball_bbox(ball_pos):
    return ball_pos[0]-BALL_RADIUS, ball_pos[1]-BALL_RADIUS, ball_pos[0]+BALL_RADIUS, ball_pos[1]+BALL_RADIUS

def brick_bbox(brick_pos,BRICK):
	return brick_pos[0]-BRICK['radius'], brick_pos[1]-BRICK['radius'], brick_pos[0]+BRICK['radius'], brick_pos[1]+BRICK['radius']

def reset_ball():
	global ball, ball_pos, ball_vel,slime_vel,slime,m1,m2
	ball_pos = [WIDTH/4., HEIGHT/2]
	canvas.coords(ball, ball_bbox(ball_pos))
	canvas.coords(slime,WIDTH/4.-SLIME_R,HEIGHT-SLIME_R,WIDTH/4.+SLIME_R,HEIGHT+SLIME_R)
	slime_vel = [0.,0,]
	ball_vel = [0,0]
	m1 = SLIME_MASS
	m2 = BALL_MASS

def reset_game():
    global ball, ball_pos, ball_vel,slime_vel,slime,m1,m2,bricks
    canvas.delete('all')
    new_game()
    draw_movable_items()
    draw_scores()
    reset_ball()
    bricks = slv.level_3(canvas)

def game_over():
    global score,bricks,canvas
    canvas.delete('all')
    canvas.create_text(WIDTH/2.,HEIGHT/2.,text='GAME OVER',font=('TkDefaultFont',80),fill=LINE_COLOUR)
    score_end = canvas.create_text((WIDTH/2), 40, text='SCORE:{}'.format(score),
                                          font=('TkDefaultFont',40),
                                          fill=LINE_COLOUR)

    canvas.create_text(HEIGHT/2.+80,WIDTH/2.+80,text='PRESS R TO RESTART',font=('TkDefaultFont',80),fill=LINE_COLOUR)
    score = 0
    return []



def draw_movable_items():
    global ball, ball_pos, slime
    ball_pos   = [WIDTH/2., HEIGHT/2.]
    ball       = canvas.create_oval(ball_bbox(ball_pos),fill=BALL_COLOUR)
    slime      = canvas.create_arc((WIDTH/4.)-SLIME_R,HEIGHT-SLIME_R,(WIDTH/4.)+SLIME_R,HEIGHT+SLIME_R, \
                                          fill=SLIME_COLOUR,extent=180)
def new_game():
    global slime_vel
    global score, score_label
    slime_vel = [0.,0.]
    score = 0
    canvas.itemconfigure(score_label,text=str(score))
    reset_ball()

def find_centre(coords):
	x0 = coords[0]
	y0 = coords[1]
	x1 = coords[2]
	y1 = coords[3]
	x = (x0 + x1)/2.
	y = (y0 + y1)/2.
	return x,y

def collision(v1,x1,m1,v2,x2,m2):   
	v1 = np.array(v1)
	x1 = np.array(x1)
	v2 = np.array(v2)
	x2 = np.array(x2)
	newv1 = v1-((2.*m2/(m2+m1))*np.dot((v1-v2),(x1-x2))/np.linalg.norm(x1-x2)**2.)*(x1-x2)
	newv2 = v2-((2.*m1/(m1+m2))*np.dot((v2-v1),(x2-x1))/np.linalg.norm(x2-x1)**2.)*(x2-x1)
	
	return newv1,newv2
	


def dynamics():
	global score,ball_pos, ball_vel,slime_vel,m1,m2,collide,jump,bricks
	bx,by      = find_centre(canvas.coords(ball))
	sx,sy      = find_centre(canvas.coords(slime))
	
	if sy < HEIGHT: 
		jump = True
	else:
		jump = False
	
	vec        = np.array([bx-sx,by-sy])
	mag        = np.sqrt(vec[0]**2. + vec[1]**2.)
	if (mag >= (SLIME_R+BALL_R)): 
		collide  = False
	
	canvas.move(slime,slime_vel[0],slime_vel[1])
	canvas.move(ball,ball_vel[0],ball_vel[1])
	
	if canvas.coords(slime)[3]>HEIGHT+SLIME_R:
		x0 = canvas.coords(slime)[0]
		x1 = canvas.coords(slime)[2]
		canvas.coords(slime,x0,HEIGHT-SLIME_R,x1,HEIGHT+SLIME_R)
		slime_vel[1] = 0.
	if jump and canvas.coords(slime)[3]<(HEIGHT+SLIME_R): slime_vel[1] += 10.*10.e-3
	
		
	if canvas.coords(slime)[0]<=0:
		y0 = canvas.coords(slime)[1]
		y1 = canvas.coords(slime)[3]
		canvas.coords(slime,0,y0,2*SLIME_R,y1)
		slime_vel[0] = 0
	elif canvas.coords(slime)[2]>=WIDTH:
		y0 = canvas.coords(slime)[1]
		y1 = canvas.coords(slime)[3]
		canvas.coords(slime,WIDTH - 2*SLIME_R,y0,WIDTH,y1)
		slime_vel[0] = 0
	
	if canvas.coords(ball)[1] <= 0:
		ball_vel[1] = -.9*ball_vel[1]
	
	if collide == False:
		bx,by      = find_centre(canvas.coords(ball))
		sx,sy      = find_centre(canvas.coords(slime))
		vec        = np.array([bx-sx,by-sy])
		mag        = np.sqrt(vec[0]**2. + vec[1]**2.)
		if mag <= (SLIME_R+BALL_R):
			collide = True
			bX = np.array([bx,by])
			sX = np.array([sx,sy])
			slime_vel,ball_vel = collision(slime_vel,sX,m1,ball_vel,bX,m2)
		else:
			pass
		if (canvas.coords(ball)[3]>=HEIGHT):
			ball_vel[1] = -.9*ball_vel[1]
			xb0 = canvas.coords(ball)[0]
			xb1 = canvas.coords(ball)[2]
			canvas.coords(ball,xb0,HEIGHT-BALL_RADIUS*2.,xb1,HEIGHT)
	if collide:
		pass
	else:
		ball_vel[1]   += 10.*10.e-3
	print 'here'	
	for BRICK in bricks:
		O  = np.array(find_centre(canvas.coords(BRICK['tag'])))
		OS = np.array(find_centre(canvas.coords(slime)))
		mag = np.linalg.norm(O-OS)
		if mag <= (SLIME_R+BRICK['radius']):
			reset_ball()
			score -= 5
			canvas.itemconfigure(score_label,text=str(score))
			if score < 0: 
				bricks = game_over()
				print 'game over starts here'	
				canvas.after_cancel(dynamics)
	for BRICK in bricks:
		O  = np.array(find_centre(canvas.coords(BRICK['tag'])))
		OB = np.array(find_centre(canvas.coords(ball)))
		mag = np.linalg.norm(O-OB)
		if mag <= (BALL_R+BRICK['radius']) and BRICK['ballcol']==False:
			oldv = [0.,0.]
			oldv[0] = BRICK['xvel']
			oldv[1] = BRICK['yvel']
			ball_vel,newv = collision(ball_vel,OB,m1,oldv,O,BRICK['mass'])
			BRICK['xvel'] = newv[0]
			BRICK['yvel'] = newv[1]
			BRICK['ballcol'] = True
			BRICK['HP']     -= 1
			score += 1
			if BRICK['color']=='blu':
				BRICK['radius'] *= 1.1
				canvas.coords(BRICK['tag'],brick_bbox(O,BRICK))

			if BRICK['color']=='red':
				BRICK['mass'] *= 1.5
			
			if BRICK['color']=='mag':
				BRICK['mass'] *= .65
			
			if BRICK['color']=='cya':
				BRICK['radius'] *= .9
				BRICK['mass'] *= .9
				canvas.coords(BRICK['tag'],brick_bbox(O,BRICK))
			
			canvas.itemconfigure(score_label,text=str(score))
		else:
			BRICK['ballcol'] = False
        
	for BRICK in bricks:
		O1                  = np.array(find_centre(canvas.coords(BRICK['tag'])))
		i = 0
		for obj in bricks:
			i+=1
			if BRICK['tag'] == obj['tag']:
				pass
			else:	
				O   = np.array(find_centre(canvas.coords(obj['tag'])))
				mag = np.linalg.norm(O1-O)
				if (mag <= (obj['radius']+BRICK['radius']) and BRICK['collide']==False):
					oldv = [0.,0.]
					v    = [0.,0.]
					oldv[0] = BRICK['xvel']
					oldv[1] = BRICK['yvel']
					v[0]    = obj['xvel']
					v[1]    = obj['yvel']
					v2,newv = collision(v,O,obj['mass'],oldv,O1,BRICK['mass'])
					BRICK['xvel']   = newv[0]
					BRICK['yvel']   = newv[1]
					obj['xvel']     = v2[0]
					obj['yvel']     = v2[1]
					obj['collide']  = True
					BRICK['collide']= True
				elif mag > (obj['radius']+BRICK['radius']):
					obj['collide']   = False
					BRICK['collide'] = False

	for BRICK in bricks:
		if canvas.coords(BRICK['tag'])[2]>= WIDTH:
			BRICK['xvel'] = -1.*BRICK['xvel']
		elif canvas.coords(BRICK['tag'])[0]<= 0:
			BRICK['xvel'] = -1.*BRICK['xvel']
		if canvas.coords(BRICK['tag'])[1] <= 0:
			BRICK['yvel'] = -1.*BRICK['yvel']
		elif canvas.coords(BRICK['tag'])[3]>= HEIGHT:
			BRICK['yvel'] = -1.*BRICK['yvel']
	for BRICK in bricks:
		canvas.move(BRICK['tag'],BRICK['xvel'],BRICK['yvel'])
		if BRICK['HP'] == 0:
			canvas.delete(BRICK['tag'])
			bricks.remove(BRICK)
			score += 10
			canvas.itemconfigure(score_label,text=str(score))


	if canvas.coords(ball)[2] >= WIDTH:
		x0 = WIDTH - 2.*BALL_R
		x1 = WIDTH
		y0 = canvas.coords(ball)[1]
		y1 = canvas.coords(ball)[3]
		canvas.coords(ball,x0,y0,x1,y1)
		ball_vel[0] = -0.9*ball_vel[0]

	if canvas.coords(ball)[0] <= 0:
	    ball_vel[0] = -0.9*ball_vel[0]

	canvas.after(10,dynamics)


def KeyPressed(event):
    global slime_vel,jump,collide
    if event.char == 'a':
        slime_vel[0] = -1.*slime_acc
    elif event.char == 'd':
        slime_vel[0] = slime_acc
    elif event.char == 'w':
        if jump == False: 
            slime_vel[1] = -1.*slime_acc/2.
        else:
            pass
    elif event.char == 'r':
		reset_game()


def KeyReleased(event):
    global slime_vel,jump
    if event.char == 'a':
        slime_vel[0] = 0.
    elif event.char == 'd':
        slime_vel[0] = 0.
    elif event.char == 'w':
        pass
    elif event.char == 'r':
        pass

def draw_scores():
    global score_label
    score_label = canvas.create_text((WIDTH/2)-40, 40, text='0',\
                                          font=('TkDefaultFont',40),\
                                          fill=LINE_COLOUR)


# Create master frame and drawing canvas.
frame = Tk()
frame.title('Slime Ball')
canvas = Canvas(frame, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack()

#canvas.create_line(WIDTH/2, HEIGHT-1.5*SLIME_R, WIDTH/2, HEIGHT, fill=LINE_COLOUR)
#canvas.create_line(PAD_WIDTH,0, PAD_WIDTH,HEIGHT, fill=LINE_COLOUR)
#canvas.create_line(WIDTH-PAD_WIDTH,0, WIDTH-PAD_WIDTH,HEIGHT, fill=LINE_COLOUR)

# Register key event handlers
frame.bind('<Key>', KeyPressed)
frame.bind('<KeyRelease>', KeyReleased)

# Draw the ball and slimes
draw_movable_items()

resetButton = Button(frame, text ="Reset", command = new_game)
resetButton.pack()

draw_scores()
new_game()
reset_game()

dynamics()
frame.mainloop()
