from Tkinter import *
import numpy as np
import string
import random

# Red brick: Largest ball, increases mass after each hit.
BRICK_R_r   = 60.
BRICK_R_m   = 100
BRICK_R_COL = 'red'
BRICK_R_hp  = 5.

# Blue brick: Smaller ball, increases size after each hit. Lightest.
BRICK_B_r   = 50.   
BRICK_B_m   = 100.
BRICK_B_COL = 'blue'
BRICK_B_hp  = 15.

# Magenta brick: Smallest ball. halves weight in each hit.
BRICK_M_r   = 40.   
BRICK_M_m   = 200.
BRICK_M_COL = 'magenta'
BRICK_M_hp  = 20.

# Cyan brick: Decreases in size on each hit. Most HP. Weighs less.
BRICK_C_r   = 50.   
BRICK_C_m   = 200.
BRICK_C_COL = 'cyan'
BRICK_C_hp  = 15.

def initialise_levels(W,H,B_R,S_R,B_M,S_M):
	global WIDTH,HEIGHT,BALL_R,SLIME_R,BALL_MASS,SLIME_MASS
	WIDTH = W
	HEIGHT = H
	BALL_R = B_R
	SLIME_R = S_R
	BALL_MASS = B_M
	SLIME_MASS = S_M
	
def level_1(canvas):

	rb1pos    = [WIDTH/2.-BRICK_R_r,         HEIGHT/4.]
	rb2pos    = [WIDTH/2.-BRICK_R_r,      3.*HEIGHT/4.]
	rb3pos    = [3.*WIDTH/4.-2.*BRICK_R_r,   HEIGHT/2.]
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
	redb3 = {'radius': BRICK_R_r,'mass': BRICK_R_m, 'tag': redbrick3,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_R_hp,
					'color':'red','start_pos': rb2pos}
	bricks  = [redb1,redb2,redb3]
	return bricks

def level_2(canvas):

	bb1pos    = [1.*WIDTH/3.-BRICK_B_r,   HEIGHT/4.]
	bb2pos    = [2.*WIDTH/3.-BRICK_B_r,   HEIGHT/4.]
	bb3pos    = [3.*WIDTH/3.-BRICK_B_r,   HEIGHT/4.]
	blubrick1 = canvas.create_oval(bb1pos[0]-BRICK_B_r,bb1pos[1]+BRICK_B_r,bb1pos[0]+BRICK_B_r,bb1pos[1]-BRICK_B_r, 
                                          fill=BRICK_B_COL)
	blubrick2 = canvas.create_oval(bb2pos[0]-BRICK_B_r,bb2pos[1]+BRICK_B_r,bb2pos[0]+BRICK_B_r,bb2pos[1]-BRICK_B_r, 
                                          fill=BRICK_B_COL)
	blubrick3 = canvas.create_oval(bb3pos[0]-BRICK_B_r,bb3pos[1]+BRICK_B_r,bb3pos[0]+BRICK_B_r,bb3pos[1]-BRICK_B_r, 
                                          fill=BRICK_B_COL)
	blub1 = {'radius': BRICK_B_r,'mass': BRICK_B_m, 'tag': blubrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'blu','start_pos': bb1pos}
	blub2 = {'radius': BRICK_B_r,'mass': BRICK_B_m, 'tag': blubrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'blu','start_pos': bb2pos}
	blub3 = {'radius': BRICK_B_r,'mass': BRICK_B_m, 'tag': blubrick3,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'blu','start_pos': bb3pos}
	bricks  = [blub1,blub2,blub3]
	return bricks

def level_3(canvas):

	rb1pos    = [WIDTH-BRICK_R_r,         HEIGHT/4.]
	rb2pos    = [WIDTH-BRICK_R_r,      3.*HEIGHT/4.]
	bb1pos    = [2.*WIDTH/3.-BRICK_B_r,   HEIGHT/2.]
	mb1pos    = [WIDTH/2.-BRICK_M_r,   HEIGHT/2.]
	redbrick1 = canvas.create_oval(rb1pos[0]-BRICK_R_r,rb1pos[1]+BRICK_R_r,rb1pos[0]+BRICK_R_r,rb1pos[1]-BRICK_R_r, 
                                          fill=BRICK_R_COL)
	redbrick2 = canvas.create_oval(rb2pos[0]-BRICK_R_r,rb2pos[1]+BRICK_R_r,rb2pos[0]+BRICK_R_r,rb2pos[1]-BRICK_R_r, 
                                          fill=BRICK_R_COL)
	blubrick1 = canvas.create_oval(bb1pos[0]-BRICK_B_r,bb1pos[1]+BRICK_B_r,bb1pos[0]+BRICK_B_r,bb1pos[1]-BRICK_B_r, 
                                          fill=BRICK_B_COL)
	magbrick1 = canvas.create_oval(mb1pos[0]-BRICK_M_r,mb1pos[1]+BRICK_M_r,mb1pos[0]+BRICK_M_r,mb1pos[1]-BRICK_M_r, 
                                          fill=BRICK_M_COL)
	redb1 = {'radius': BRICK_R_r,'mass': BRICK_R_m, 'tag': redbrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_R_hp,
					'color':'red','start_pos': rb1pos}
	redb2 = {'radius': BRICK_R_r,'mass': BRICK_R_m, 'tag': redbrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_R_hp,
					'color':'red','start_pos': rb2pos}
	blub1 = {'radius': BRICK_B_r,'mass': BRICK_B_m, 'tag': blubrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'blu','start_pos': bb1pos}
	magb1 = {'radius': BRICK_M_r,'mass': BRICK_M_m, 'tag': magbrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'mag','start_pos': mb1pos}
	bricks  = [redb1,redb2,blub1,magb1]
	bricks_original  = [redb1,redb2,blub1,magb1]
	return bricks

def level_4(canvas):

	mb1pos    = [WIDTH-BRICK_M_r,         HEIGHT/4.]
	mb2pos    = [WIDTH-BRICK_M_r,      3.*HEIGHT/4.]
	mb3pos    = [WIDTH-BRICK_M_r,         HEIGHT/2.]
	cb1pos    = [WIDTH-3.*BRICK_C_r,      HEIGHT/2.]
	magbrick1 = canvas.create_oval(mb1pos[0]-BRICK_M_r,mb1pos[1]+BRICK_M_r,mb1pos[0]+BRICK_M_r,mb1pos[1]-BRICK_M_r, 
                                          fill=BRICK_M_COL)
	magbrick2 = canvas.create_oval(mb2pos[0]-BRICK_M_r,mb2pos[1]+BRICK_M_r,mb2pos[0]+BRICK_M_r,mb2pos[1]-BRICK_M_r, 
                                          fill=BRICK_M_COL)
	magbrick3 = canvas.create_oval(mb3pos[0]-BRICK_M_r,mb3pos[1]+BRICK_M_r,mb3pos[0]+BRICK_M_r,mb3pos[1]-BRICK_M_r, 
                                          fill=BRICK_M_COL)
	cyabrick1 = canvas.create_oval(cb1pos[0]-BRICK_C_r,cb1pos[1]+BRICK_C_r,cb1pos[0]+BRICK_C_r,cb1pos[1]-BRICK_C_r, 
                                          fill=BRICK_C_COL)
	magb1 = {'radius': BRICK_M_r,'mass': BRICK_M_m, 'tag': magbrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'mag','start_pos': mb1pos}
	magb2 = {'radius': BRICK_M_r,'mass': BRICK_M_m, 'tag': magbrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'mag','start_pos': mb2pos}
	magb3 = {'radius': BRICK_M_r,'mass': BRICK_M_m, 'tag': magbrick3,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'mag','start_pos': mb3pos}
	cyab1 = {'radius': BRICK_C_r,'mass': BRICK_C_m, 'tag': cyabrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_C_hp,
					'color':'cya','start_pos': cb1pos}
	bricks  = [magb1,magb2,magb3,cyab1]
	return bricks

def level_5(canvas):

	mb1pos    = [WIDTH-BRICK_M_r,         HEIGHT/4.]
	mb2pos    = [WIDTH-BRICK_M_r,      3.*HEIGHT/4.]
	mb3pos    = [WIDTH-BRICK_M_r,         HEIGHT/2.]
	cb1pos    = [WIDTH-3.*BRICK_C_r,      HEIGHT/2.]
	cb2pos    = [WIDTH-3.*BRICK_C_r,   3.*HEIGHT/4.]
	cb3pos    = [WIDTH-3.*BRICK_C_r,      HEIGHT/4.]
	magbrick1 = canvas.create_oval(mb1pos[0]-BRICK_M_r,mb1pos[1]+BRICK_M_r,mb1pos[0]+BRICK_M_r,mb1pos[1]-BRICK_M_r, 
                                          fill=BRICK_M_COL)
	magbrick2 = canvas.create_oval(mb2pos[0]-BRICK_M_r,mb2pos[1]+BRICK_M_r,mb2pos[0]+BRICK_M_r,mb2pos[1]-BRICK_M_r, 
                                          fill=BRICK_M_COL)
	magbrick3 = canvas.create_oval(mb3pos[0]-BRICK_M_r,mb3pos[1]+BRICK_M_r,mb3pos[0]+BRICK_M_r,mb3pos[1]-BRICK_M_r, 
                                          fill=BRICK_M_COL)
	cyabrick1 = canvas.create_oval(cb1pos[0]-BRICK_C_r,cb1pos[1]+BRICK_C_r,cb1pos[0]+BRICK_C_r,cb1pos[1]-BRICK_C_r, 
                                          fill=BRICK_C_COL)
	cyabrick2 = canvas.create_oval(cb2pos[0]-BRICK_C_r,cb2pos[1]+BRICK_C_r,cb2pos[0]+BRICK_C_r,cb2pos[1]-BRICK_C_r, 
                                          fill=BRICK_C_COL)
	cyabrick3 = canvas.create_oval(cb3pos[0]-BRICK_C_r,cb3pos[1]+BRICK_C_r,cb3pos[0]+BRICK_C_r,cb3pos[1]-BRICK_C_r, 
                                          fill=BRICK_C_COL)
	magb1 = {'radius': BRICK_M_r,'mass': BRICK_M_m, 'tag': magbrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'mag','start_pos': mb1pos}
	magb2 = {'radius': BRICK_M_r,'mass': BRICK_M_m, 'tag': magbrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'mag','start_pos': mb2pos}
	magb3 = {'radius': BRICK_M_r,'mass': BRICK_M_m, 'tag': magbrick3,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'mag','start_pos': mb3pos}
	cyab1 = {'radius': BRICK_C_r,'mass': BRICK_C_m, 'tag': cyabrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_C_hp,
					'color':'cya','start_pos': cb1pos}
	cyab2 = {'radius': BRICK_C_r,'mass': BRICK_C_m, 'tag': cyabrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_C_hp,
					'color':'cya','start_pos': cb1pos}
	cyab3 = {'radius': BRICK_C_r,'mass': BRICK_C_m, 'tag': cyabrick3,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_C_hp,
					'color':'cya','start_pos': cb1pos}
	bricks  = [magb1,magb2,magb3,cyab1,cyab2,cyab3]
	return bricks
