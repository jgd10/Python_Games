from Tkinter import *
import numpy as np
import string
import random
import math

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

# Grey brick: Obstacle ball. can not be destroyed, does not kill slime. Gets in the way
BRICK_G_r   = 55.   
BRICK_G_m   = 100.
BRICK_G_COL = '#808080'
BRICK_G_hp = float('inf') 

# White brick: Obstacle ball. can not be destroyed, does not kill slime, infinite mass 
BRICK_W_r   = 45.   
BRICK_W_m   = 1.e9
BRICK_W_COL = '#FFFFFF'
BRICK_W_hp = float('inf') 

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
	return canvas,bricks

def level_3(canvas):
	phi = 30
	phi *= math.pi/180.
	
	rb1pos    = [WIDTH/4,         HEIGHT/3.]
	bb1pos    = [WIDTH/4,         HEIGHT/3.+BRICK_R_r+BRICK_B_r]
	bb2pos    = [WIDTH/4-(BRICK_R_r+BRICK_B_r)*math.cos(phi),HEIGHT/3.-(BRICK_R_r+BRICK_B_r)*math.sin(phi)]
	bb3pos    = [WIDTH/4+(BRICK_R_r+BRICK_B_r)*math.cos(phi),HEIGHT/3.-(BRICK_R_r+BRICK_B_r)*math.sin(phi)]
	
	rb2pos    = [3.*WIDTH/4,         HEIGHT/3.]
	bb4pos    = [3.*WIDTH/4,         HEIGHT/3.+BRICK_R_r+BRICK_B_r]
	bb5pos    = [3.*WIDTH/4-(BRICK_R_r+BRICK_B_r)*math.cos(phi),HEIGHT/3.-(BRICK_R_r+BRICK_B_r)*math.sin(phi)]
	bb6pos    = [3.*WIDTH/4+(BRICK_R_r+BRICK_B_r)*math.cos(phi),HEIGHT/3.-(BRICK_R_r+BRICK_B_r)*math.sin(phi)]
	
	phi = 30
	phi *= math.pi/180.
	bb7pos    = [WIDTH/2,         2.*HEIGHT/3.]
	rb3pos    = [WIDTH/2,         2.*HEIGHT/3.-BRICK_R_r-BRICK_B_r]
	rb4pos    = [WIDTH/2-(BRICK_R_r+BRICK_B_r)*math.cos(phi),2.*HEIGHT/3.+(BRICK_R_r+BRICK_B_r)*math.sin(phi)]
	rb5pos    = [WIDTH/2+(BRICK_R_r+BRICK_B_r)*math.cos(phi),2.*HEIGHT/3.+(BRICK_R_r+BRICK_B_r)*math.sin(phi)]


	
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
	blubrick4 = canvas.create_oval(bb4pos[0]-BRICK_B_r,bb4pos[1]+BRICK_B_r,bb4pos[0]+BRICK_B_r,bb4pos[1]-BRICK_B_r, 
                                          fill=BRICK_B_COL)
	blubrick5 = canvas.create_oval(bb5pos[0]-BRICK_B_r,bb5pos[1]+BRICK_B_r,bb5pos[0]+BRICK_B_r,bb5pos[1]-BRICK_B_r, 
                                          fill=BRICK_B_COL)
	blubrick6 = canvas.create_oval(bb6pos[0]-BRICK_B_r,bb6pos[1]+BRICK_B_r,bb6pos[0]+BRICK_B_r,bb6pos[1]-BRICK_B_r, 
                                          fill=BRICK_B_COL)
	blubrick7 = canvas.create_oval(bb7pos[0]-BRICK_B_r,bb7pos[1]+BRICK_B_r,bb7pos[0]+BRICK_B_r,bb7pos[1]-BRICK_B_r, 
                                          fill=BRICK_B_COL)
	blub4 = {'radius': BRICK_B_r,'mass': BRICK_B_m, 'tag': blubrick4,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'blu','start_pos': bb4pos}
	blub5 = {'radius': BRICK_B_r,'mass': BRICK_B_m, 'tag': blubrick5,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'blu','start_pos': bb5pos}
	blub6 = {'radius': BRICK_B_r,'mass': BRICK_B_m, 'tag': blubrick6,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'blu','start_pos': bb6pos}
	blub7 = {'radius': BRICK_B_r,'mass': BRICK_B_m, 'tag': blubrick7,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'blu','start_pos': bb7pos}
	redbrick4 = canvas.create_oval(rb4pos[0]-BRICK_R_r,rb4pos[1]+BRICK_R_r,rb4pos[0]+BRICK_R_r,rb4pos[1]-BRICK_R_r, 
                                          fill=BRICK_R_COL)
	redbrick5 = canvas.create_oval(rb5pos[0]-BRICK_R_r,rb5pos[1]+BRICK_R_r,rb5pos[0]+BRICK_R_r,rb5pos[1]-BRICK_R_r, 
                                          fill=BRICK_R_COL)
	redb4 = {'radius': BRICK_R_r,'mass': BRICK_R_m, 'tag': redbrick4,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_R_hp,
					'color':'red','start_pos': rb4pos}
	redb5 = {'radius': BRICK_R_r,'mass': BRICK_R_m, 'tag': redbrick5,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_R_hp,
					'color':'red','start_pos': rb5pos}
	bricks  = [redb1,redb2,redb3,redb4,redb5,blub1,blub2,blub3,blub4,blub5,blub6,blub7]
	return canvas,bricks

def level_4(canvas):

	gb1pos    = [WIDTH/2.-BRICK_G_r,         HEIGHT/4.]
	gb2pos    = [WIDTH/2.-BRICK_G_r,      3.*HEIGHT/4.]
	gb3pos    = [WIDTH/2.+BRICK_G_r,         HEIGHT/2.]

	bb1pos    = [WIDTH/2.+BRICK_G_r,         HEIGHT/4.]
	bb2pos    = [WIDTH/2.+BRICK_G_r,      3.*HEIGHT/4.]
	bb3pos    = [WIDTH/2.-BRICK_G_r,         HEIGHT/2.]

	gb4pos    = [WIDTH/2.-BRICK_G_r+4.*BRICK_G_r,   HEIGHT/4.]
	gb5pos    = [WIDTH/2.-BRICK_G_r+4.*BRICK_G_r,3.*HEIGHT/4.]
	gb6pos    = [WIDTH/2.+BRICK_G_r+4.*BRICK_G_r,   HEIGHT/2.]
	                                                     
	bb4pos    = [WIDTH/2.+BRICK_G_r+4.*BRICK_G_r,   HEIGHT/4.]
	bb5pos    = [WIDTH/2.+BRICK_G_r+4.*BRICK_G_r,3.*HEIGHT/4.]
	bb6pos    = [WIDTH/2.-BRICK_G_r+4.*BRICK_G_r,   HEIGHT/2.]
	
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
	grybrick1 = canvas.create_oval(gb1pos[0]-BRICK_G_r,gb1pos[1]+BRICK_G_r,gb1pos[0]+BRICK_G_r,gb1pos[1]-BRICK_G_r, 
                                          fill=BRICK_G_COL)
	grybrick2 = canvas.create_oval(gb2pos[0]-BRICK_G_r,gb2pos[1]+BRICK_G_r,gb2pos[0]+BRICK_G_r,gb2pos[1]-BRICK_G_r, 
                                          fill=BRICK_G_COL)
	grybrick3 = canvas.create_oval(gb3pos[0]-BRICK_G_r,gb3pos[1]+BRICK_G_r,gb3pos[0]+BRICK_G_r,gb3pos[1]-BRICK_G_r, 
                                          fill=BRICK_G_COL)
	gryb1 = {'radius': BRICK_G_r,'mass': BRICK_G_m, 'tag': grybrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_G_hp,
					'color':'gry','start_pos': gb1pos}
	gryb2 = {'radius': BRICK_G_r,'mass': BRICK_G_m, 'tag': grybrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_G_hp,
					'color':'gry','start_pos': gb2pos}
	gryb3 = {'radius': BRICK_G_r,'mass': BRICK_G_m, 'tag': grybrick3,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_G_hp,
					'color':'gry','start_pos': gb3pos}
	blubrick4 = canvas.create_oval(bb4pos[0]-BRICK_B_r,bb4pos[1]+BRICK_B_r,bb4pos[0]+BRICK_B_r,bb4pos[1]-BRICK_B_r, 
                                          fill=BRICK_B_COL)
	blubrick5 = canvas.create_oval(bb5pos[0]-BRICK_B_r,bb5pos[1]+BRICK_B_r,bb5pos[0]+BRICK_B_r,bb5pos[1]-BRICK_B_r, 
                                          fill=BRICK_B_COL)
	blubrick6 = canvas.create_oval(bb6pos[0]-BRICK_B_r,bb6pos[1]+BRICK_B_r,bb6pos[0]+BRICK_B_r,bb6pos[1]-BRICK_B_r, 
                                          fill=BRICK_B_COL)
	blub4 = {'radius': BRICK_B_r,'mass': BRICK_B_m, 'tag': blubrick4,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'blu','start_pos': bb4pos}
	blub5 = {'radius': BRICK_B_r,'mass': BRICK_B_m, 'tag': blubrick5,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'blu','start_pos': bb5pos}
	blub6 = {'radius': BRICK_B_r,'mass': BRICK_B_m, 'tag': blubrick6,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'blu','start_pos': bb6pos}
	grybrick4 = canvas.create_oval(gb4pos[0]-BRICK_G_r,gb4pos[1]+BRICK_G_r,gb4pos[0]+BRICK_G_r,gb4pos[1]-BRICK_G_r, 
                                          fill=BRICK_G_COL)
	grybrick5 = canvas.create_oval(gb5pos[0]-BRICK_G_r,gb5pos[1]+BRICK_G_r,gb5pos[0]+BRICK_G_r,gb5pos[1]-BRICK_G_r, 
                                          fill=BRICK_G_COL)
	grybrick6 = canvas.create_oval(gb6pos[0]-BRICK_G_r,gb6pos[1]+BRICK_G_r,gb6pos[0]+BRICK_G_r,gb6pos[1]-BRICK_G_r, 
                                          fill=BRICK_G_COL)
	gryb4 = {'radius': BRICK_G_r,'mass': BRICK_G_m, 'tag': grybrick4,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_G_hp,
					'color':'gry','start_pos': gb4pos}
	gryb5 = {'radius': BRICK_G_r,'mass': BRICK_G_m, 'tag': grybrick5,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_G_hp,
					'color':'gry','start_pos': gb5pos}
	gryb6 = {'radius': BRICK_G_r,'mass': BRICK_G_m, 'tag': grybrick6,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_G_hp,
					'color':'gry','start_pos': gb6pos}
	bricks  = [gryb1,gryb2,gryb3,gryb4,gryb5,gryb6,blub1,blub2,blub3,blub4,blub5,blub6]
	return canvas,bricks
def level_5(canvas):

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
	return canvas,bricks

def level_8(canvas):

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
	return canvas,bricks

def level_9(canvas):

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
	return canvas,bricks

def level_6(canvas):

	
	phi = 30
	phi *= math.pi/180.
	wb1pos    = [WIDTH/2,         HEIGHT/2.]
	mb1pos    = [WIDTH/2,         HEIGHT/2.-BRICK_W_r-BRICK_M_r]
	mb2pos    = [WIDTH/2-(BRICK_M_r+BRICK_W_r)*math.cos(phi),HEIGHT/2.+(BRICK_M_r+BRICK_W_r)*math.sin(phi)]
	mb3pos    = [WIDTH/2+(BRICK_M_r+BRICK_W_r)*math.cos(phi),HEIGHT/2.+(BRICK_M_r+BRICK_W_r)*math.sin(phi)]
	
	magbrick1 = canvas.create_oval(mb1pos[0]-BRICK_M_r,mb1pos[1]+BRICK_M_r,mb1pos[0]+BRICK_M_r,mb1pos[1]-BRICK_M_r, 
                                          fill=BRICK_M_COL)
	magbrick2 = canvas.create_oval(mb2pos[0]-BRICK_M_r,mb2pos[1]+BRICK_M_r,mb2pos[0]+BRICK_M_r,mb2pos[1]-BRICK_M_r, 
                                          fill=BRICK_M_COL)
	magbrick3 = canvas.create_oval(mb3pos[0]-BRICK_M_r,mb3pos[1]+BRICK_M_r,mb3pos[0]+BRICK_M_r,mb3pos[1]-BRICK_M_r, 
                                          fill=BRICK_M_COL)
	whtbrick1 = canvas.create_oval(wb1pos[0]-BRICK_W_r,wb1pos[1]+BRICK_W_r,wb1pos[0]+BRICK_W_r,wb1pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtb1 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'wht','start_pos': wb1pos}
	magb1 = {'radius': BRICK_M_r,'mass': BRICK_M_m, 'tag': magbrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'mag','start_pos': mb1pos}
	magb2 = {'radius': BRICK_M_r,'mass': BRICK_M_m, 'tag': magbrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'mag','start_pos': mb2pos}
	magb3 = {'radius': BRICK_M_r,'mass': BRICK_M_m, 'tag': magbrick3,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_B_hp,
					'color':'mag','start_pos': mb3pos}
	bricks  = [magb1,magb2,magb3,whtb1]
	return canvas,bricks
def level_7(canvas):

	wb1pos    = [0,          HEIGHT/2.]
	wb2pos    = [WIDTH/4.,   HEIGHT/2.]
	wb3pos    = [WIDTH/2.,   HEIGHT/2.]
	wb4pos    = [3.*WIDTH/4.,HEIGHT/2.]
	wb5pos    = [WIDTH,      HEIGHT/2.]
	

	cb1pos    = [WIDTH/4.,      HEIGHT/4.]
	cb2pos    = [WIDTH/2.,      HEIGHT/4.]
	cb3pos    = [3.*WIDTH/4.,   HEIGHT/4.]

	whtbrick1 = canvas.create_oval(wb1pos[0]-BRICK_W_r,wb1pos[1]+BRICK_W_r,wb1pos[0]+BRICK_W_r,wb1pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtbrick2 = canvas.create_oval(wb2pos[0]-BRICK_W_r,wb2pos[1]+BRICK_W_r,wb2pos[0]+BRICK_W_r,wb2pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtbrick3 = canvas.create_oval(wb3pos[0]-BRICK_W_r,wb3pos[1]+BRICK_W_r,wb3pos[0]+BRICK_W_r,wb3pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtbrick4 = canvas.create_oval(wb4pos[0]-BRICK_W_r,wb4pos[1]+BRICK_W_r,wb4pos[0]+BRICK_W_r,wb4pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtbrick5 = canvas.create_oval(wb5pos[0]-BRICK_W_r,wb5pos[1]+BRICK_W_r,wb5pos[0]+BRICK_W_r,wb5pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	
	cyabrick1 = canvas.create_oval(cb1pos[0]-BRICK_C_r,cb1pos[1]+BRICK_C_r,cb1pos[0]+BRICK_C_r,cb1pos[1]-BRICK_C_r, 
                                          fill=BRICK_C_COL)
	cyabrick2 = canvas.create_oval(cb2pos[0]-BRICK_C_r,cb2pos[1]+BRICK_C_r,cb2pos[0]+BRICK_C_r,cb2pos[1]-BRICK_C_r, 
                                          fill=BRICK_C_COL)
	cyabrick3 = canvas.create_oval(cb3pos[0]-BRICK_C_r,cb3pos[1]+BRICK_C_r,cb3pos[0]+BRICK_C_r,cb3pos[1]-BRICK_C_r, 
                                          fill=BRICK_C_COL)

	whtb1 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb1pos}
	whtb2 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb2pos}
	whtb3 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick3,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb3pos}
	whtb4 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick4,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb4pos}
	whtb5 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick5,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb5pos}
	
	cyab1 = {'radius': BRICK_C_r,'mass': BRICK_C_m, 'tag': cyabrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_C_hp,
					'color':'cya','start_pos': cb1pos}
	cyab2 = {'radius': BRICK_C_r,'mass': BRICK_C_m, 'tag': cyabrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_C_hp,
					'color':'cya','start_pos': cb2pos}
	cyab3 = {'radius': BRICK_C_r,'mass': BRICK_C_m, 'tag': cyabrick3,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_C_hp,
					'color':'cya','start_pos': cb3pos}
	bricks  = [whtb1,whtb2,whtb3,whtb4,whtb5,cyab1,cyab2,cyab3]
	return canvas,bricks

def level_2(canvas):
	rb1pos    = [WIDTH/4.,      HEIGHT/2.]
	rb2pos    = [WIDTH/2.,      HEIGHT/2.]
	rb3pos    = [3*WIDTH/4.,    HEIGHT/2.]
	
	wb1pos    = [(rb1pos[0]+rb2pos[0])/2.,  HEIGHT/2.+BRICK_R_r]
	wb2pos    = [(rb2pos[0]+rb3pos[0])/2.,  HEIGHT/2.+BRICK_R_r]
	wb3pos    = [(rb1pos[0]+rb2pos[0])/2.,  HEIGHT/2.-BRICK_R_r]
	wb4pos    = [(rb2pos[0]+rb3pos[0])/2.,  HEIGHT/2.-BRICK_R_r]
	
	
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
					'color':'red','start_pos': rb3pos}
	whtbrick1 = canvas.create_oval(wb1pos[0]-BRICK_W_r,wb1pos[1]+BRICK_W_r,wb1pos[0]+BRICK_W_r,wb1pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtbrick2 = canvas.create_oval(wb2pos[0]-BRICK_W_r,wb2pos[1]+BRICK_W_r,wb2pos[0]+BRICK_W_r,wb2pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtbrick3 = canvas.create_oval(wb3pos[0]-BRICK_W_r,wb3pos[1]+BRICK_W_r,wb3pos[0]+BRICK_W_r,wb3pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtbrick4 = canvas.create_oval(wb4pos[0]-BRICK_W_r,wb4pos[1]+BRICK_W_r,wb4pos[0]+BRICK_W_r,wb4pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtb1 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb1pos}
	whtb2 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb2pos}
	whtb3 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick3,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb3pos}
	whtb4 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick4,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb4pos}
	bricks  = [whtb1,whtb2,whtb3,whtb4,redb1,redb2,redb3]
	return canvas,bricks

def level_10(canvas):

	wb1pos    = [3.*WIDTH/4.,       3.*BRICK_W_r]
	wb2pos    = [WIDTH/2.,             HEIGHT/2.]
	wb3pos    = [WIDTH/4.,   HEIGHT-3.*BRICK_W_r]
	wb4pos    = [WIDTH/4.,          3.*BRICK_W_r]
	wb5pos    = [3.*WIDTH/4.,HEIGHT-3.*BRICK_W_r]
	
	cb1pos    = [WIDTH-BRICK_C_r,      BRICK_C_r]
	cb2pos    = [WIDTH-BRICK_C_r,   3.*BRICK_C_r]
	cb3pos    = [WIDTH-BRICK_C_r,   5.*BRICK_C_r]
	cb4pos    = [WIDTH-BRICK_C_r,   7.*BRICK_C_r]
	cb5pos    = [WIDTH-BRICK_C_r,   9.*BRICK_C_r]
	
	
	whtbrick1 = canvas.create_oval(wb1pos[0]-BRICK_W_r,wb1pos[1]+BRICK_W_r,wb1pos[0]+BRICK_W_r,wb1pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtbrick2 = canvas.create_oval(wb2pos[0]-BRICK_W_r,wb2pos[1]+BRICK_W_r,wb2pos[0]+BRICK_W_r,wb2pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtbrick3 = canvas.create_oval(wb3pos[0]-BRICK_W_r,wb3pos[1]+BRICK_W_r,wb3pos[0]+BRICK_W_r,wb3pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtbrick4 = canvas.create_oval(wb4pos[0]-BRICK_W_r,wb4pos[1]+BRICK_W_r,wb4pos[0]+BRICK_W_r,wb4pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtbrick5 = canvas.create_oval(wb5pos[0]-BRICK_W_r,wb5pos[1]+BRICK_W_r,wb5pos[0]+BRICK_W_r,wb5pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	
	cyabrick1 = canvas.create_oval(cb1pos[0]-BRICK_C_r,cb1pos[1]+BRICK_C_r,cb1pos[0]+BRICK_C_r,cb1pos[1]-BRICK_C_r, 
                                          fill=BRICK_C_COL)
	cyabrick2 = canvas.create_oval(cb2pos[0]-BRICK_C_r,cb2pos[1]+BRICK_C_r,cb2pos[0]+BRICK_C_r,cb2pos[1]-BRICK_C_r, 
                                          fill=BRICK_C_COL)
	cyabrick3 = canvas.create_oval(cb3pos[0]-BRICK_C_r,cb3pos[1]+BRICK_C_r,cb3pos[0]+BRICK_C_r,cb3pos[1]-BRICK_C_r, 
                                          fill=BRICK_C_COL)
	cyabrick4 = canvas.create_oval(cb4pos[0]-BRICK_C_r,cb4pos[1]+BRICK_C_r,cb4pos[0]+BRICK_C_r,cb4pos[1]-BRICK_C_r, 
                                          fill=BRICK_C_COL)
	cyabrick5 = canvas.create_oval(cb5pos[0]-BRICK_C_r,cb5pos[1]+BRICK_C_r,cb5pos[0]+BRICK_C_r,cb5pos[1]-BRICK_C_r, 
                                          fill=BRICK_C_COL)
	
	whtb1 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb1pos}
	whtb2 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb2pos}
	whtb3 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick3,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb3pos}
	whtb4 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick4,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb4pos}
	whtb5 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick5,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb5pos}
	
	cyab1 = {'radius': BRICK_C_r,'mass': BRICK_C_m, 'tag': cyabrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_C_hp,
					'color':'cya','start_pos': cb1pos}
	cyab2 = {'radius': BRICK_C_r,'mass': BRICK_C_m, 'tag': cyabrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_C_hp,
					'color':'cya','start_pos': cb2pos}
	cyab3 = {'radius': BRICK_C_r,'mass': BRICK_C_m, 'tag': cyabrick3,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_C_hp,
					'color':'cya','start_pos': cb3pos}
	cyab4 = {'radius': BRICK_C_r,'mass': BRICK_C_m, 'tag': cyabrick4,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_C_hp,
					'color':'cya','start_pos': cb4pos}
	cyab5 = {'radius': BRICK_C_r,'mass': BRICK_C_m, 'tag': cyabrick5,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_C_hp,
					'color':'cya','start_pos': cb5pos}
	bricks  = [cyab1,cyab2,cyab3,cyab4,cyab5,whtb1,whtb2,whtb3,whtb4,whtb5]
	return canvas,bricks

def level_11(canvas):

	wb1pos    = [WIDTH/2.,       HEIGHT]
	wb2pos    = [0,    HEIGHT]
	wb3pos    = [WIDTH,          HEIGHT]
	wb4pos    = [WIDTH,    0]
	wb5pos    = [0,          0]
	
	cb1pos    = [WIDTH/2.,      HEIGHT/2.]
	mb1pos    = [WIDTH/2.+BRICK_M_r+BRICK_C_r,      HEIGHT/2.]
	mb2pos    = [WIDTH/2.-BRICK_M_r-BRICK_C_r,      HEIGHT/2.]
	mb3pos    = [WIDTH/2.,      HEIGHT/2.+BRICK_M_r+BRICK_C_r]
	mb4pos    = [WIDTH/2.,      HEIGHT/2.-BRICK_M_r-BRICK_C_r]
	
	
	whtbrick1 = canvas.create_oval(wb1pos[0]-BRICK_W_r,wb1pos[1]+BRICK_W_r,wb1pos[0]+BRICK_W_r,wb1pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtbrick2 = canvas.create_oval(wb2pos[0]-BRICK_W_r,wb2pos[1]+BRICK_W_r,wb2pos[0]+BRICK_W_r,wb2pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtbrick3 = canvas.create_oval(wb3pos[0]-BRICK_W_r,wb3pos[1]+BRICK_W_r,wb3pos[0]+BRICK_W_r,wb3pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtbrick4 = canvas.create_oval(wb4pos[0]-BRICK_W_r,wb4pos[1]+BRICK_W_r,wb4pos[0]+BRICK_W_r,wb4pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	whtbrick5 = canvas.create_oval(wb5pos[0]-BRICK_W_r,wb5pos[1]+BRICK_W_r,wb5pos[0]+BRICK_W_r,wb5pos[1]-BRICK_W_r, 
                                          fill=BRICK_W_COL)
	
	cyabrick1 = canvas.create_oval(cb1pos[0]-BRICK_C_r,cb1pos[1]+BRICK_C_r,cb1pos[0]+BRICK_C_r,cb1pos[1]-BRICK_C_r, 
                                          fill=BRICK_C_COL)
	magbrick1 = canvas.create_oval(mb1pos[0]-BRICK_M_r,mb1pos[1]+BRICK_M_r,mb1pos[0]+BRICK_M_r,mb1pos[1]-BRICK_M_r, 
                                          fill=BRICK_M_COL)
	magbrick2 = canvas.create_oval(mb2pos[0]-BRICK_M_r,mb2pos[1]+BRICK_M_r,mb2pos[0]+BRICK_M_r,mb2pos[1]-BRICK_M_r, 
                                          fill=BRICK_M_COL)
	magbrick3 = canvas.create_oval(mb3pos[0]-BRICK_M_r,mb3pos[1]+BRICK_M_r,mb3pos[0]+BRICK_M_r,mb3pos[1]-BRICK_M_r, 
                                          fill=BRICK_M_COL)
	magbrick4 = canvas.create_oval(mb4pos[0]-BRICK_M_r,mb4pos[1]+BRICK_M_r,mb4pos[0]+BRICK_M_r,mb4pos[1]-BRICK_M_r, 
                                          fill=BRICK_M_COL)
	
	whtb1 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb1pos}
	whtb2 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb2pos}
	whtb3 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick3,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb3pos}
	whtb4 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick4,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb4pos}
	whtb5 = {'radius': BRICK_W_r,'mass': BRICK_W_m, 'tag': whtbrick5,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_W_hp,
					'color':'wht','start_pos': wb5pos}
	
	cyab1 = {'radius': BRICK_C_r,'mass': BRICK_C_m, 'tag': cyabrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_C_hp,
					'color':'cya','start_pos': cb1pos}
	magb1 = {'radius': BRICK_M_r,'mass': BRICK_M_m, 'tag': magbrick1,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_M_hp,
					'color':'mag','start_pos': mb1pos}
	magb2 = {'radius': BRICK_M_r,'mass': BRICK_M_m, 'tag': magbrick2,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_M_hp,
					'color':'mag','start_pos': mb2pos}
	magb3 = {'radius': BRICK_M_r,'mass': BRICK_M_m, 'tag': magbrick3,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_M_hp,
					'color':'mag','start_pos': mb3pos}
	magb4 = {'radius': BRICK_M_r,'mass': BRICK_M_m, 'tag': magbrick4,'xvel':0.,'yvel':0.,'collide':False,'ballcol':False,'HP':BRICK_M_hp,
					'color':'mag','start_pos': mb4pos}
	bricks  = [cyab1,magb1,magb2,magb3,magb4,whtb1,whtb2,whtb3,whtb4,whtb5]
	return canvas,bricks
