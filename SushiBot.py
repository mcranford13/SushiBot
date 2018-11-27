###############################################################################################
#																							  #	
#									Sushi Go Round Bot										  #
#										by Matthew Cranford									  #
#															aka ^graff						  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
#																							  #
###############################################################################################

#################
#   Libraries   #
#################

import ImageGrab
import os
import time 
import win32api, win32con
import ImageOps
from numpy import *

########################
#   Global Variables   #
########################
'''
This defines any and all 'magic numbers' and the like. 

Note: All global variables will be written in CAPS for ease of use.

'''

CWD = os.getcwd() #This grabs the current working directory.
X_PAD = 464
Y_PAD = 223


foodOnHand = { 'shrimp':5,
			   'rice':10,
			   'nori':10,
			   'roe':10,
			   'salmon':5,
			   'unagi':5}
			   


sushiTypes = { 2670: 'onigiri',
			   3143: 'caliroll',
			   2677: 'gunkan'}	

###############
#   Classes   #
###############


'''

Recipes

Onigiri:

2 x rice
1 x nori


California roll:

1 x rice 
1 x nori
1 x roe

gunkan maki:

1 x rice 
1 x nori
2 x roe



'''
class notReady():
	pass
	
class Blank():
	seat_1 = 8119
	seat_2 = 5986
	seat_3 = 11596
	seat_4 = 10613
	seat_5 = 7286
	seat_6 = 9119

class Cord():
	
	f_shrimp = (75,323)
	f_rice   = (95,333)
	f_nori   = (26,385)
	f_roe    = (86,381)
	f_salmon = (35,441)
	f_unagi  = (94,438)
	
 #----------------------------#
	phone = (580,358)
	
	menu_toppings = (524,269)
	
	t_shrimp = (496, 216)
	t_nori   = (495, 277)
	t_roe    = (577, 272)
	t_salmon = (491, 331)
	t_unagi  = (572, 222)
	t_exit   = (592, 336)
	
	menu_rice = (502, 292)
	buy_rice  = (520, 264)
	
	menu_sake = (507, 314)
	buy_sake  = (539, 272)
	
	delivery_norm = (484, 287)
	
 #----------------------------#
 

	
	
	
	

#-------------Functions Start---------------#


#######################
#   Screen Controls   #
#######################
	
def screenGrab(): #This grabs a screenshot and saves in the current working directory as a '.png' file.
	box = (X_PAD + 1, Y_PAD +1,X_PAD + 640, Y_PAD + 480)
	im = ImageGrab.grab()
	
	#im.save(CWD + '\\ful_snap__' + str(int(time.time())) + '.png', 'PNG') #(directory, (name, timestamp), fileformat)
	
	return im
	
def grab():
	box = (X_PAD + 1, Y_PAD +1,X_PAD + 640, Y_PAD + 480)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	print a
	return a

######################
#   Mouse Controls   #
######################

def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #This clicks the mouse down.
	time.sleep(.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) #This releases the click on the mouse.
	#print "Left Click." # Optional but nice for debugging

def leftDown():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0) #This is for holding the left button down. It will be used for dragging or holding.
	time.sleep(.1)
	print "Left Click Held"
	
def leftUp():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0) #This just releases the mouse click for us.
	time.sleep(.1)
	print "Left Click Released."
	
def mousePos(cord): #This is expecting a tulple
	win32api.SetCursorPos((X_PAD + cord[0], Y_PAD + cord[1]))
	
def get_cords():
	x,y = win32api.GetCursorPos()
	x = x - X_PAD
	y = y - Y_PAD
	print x,y	
	
	
###########################
#   Navigate start menu   #
###########################

def banner():
	print "Sushi Go Round Bot v1.0"
def start_game():
	
	print "Starting Game..."
	print "Navigating through start menus..."
	#Location of first menu
	mousePos((298,196))
	leftClick()
	time.sleep(.2)	
	
	#Location of second menu
	
	mousePos((324,388))
	leftClick()
	time.sleep(.2)	
	
	#Location of third menu
	
	mousePos((573,448))
	leftClick()
	time.sleep(.2)	
	
	#Location of fourth menu
	
	mousePos((311,378))
	leftClick()
	time.sleep(.2)	
	
	
#---------- Make Food -----------#
def makeFood(food):
	if food == "caliroll":
		print "Making a california roll..."
		foodOnHand['rice'] -= 1
		foodOnHand['nori'] -= 1
		foodOnHand['roe'] -= 1
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_nori)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_roe)
		leftClick()
		time.sleep(.1)
		foldMat()
		print "Done!"
		time.sleep(1.5)
		
		
	elif food == 'onigiri':
		print "Making a Onigiri..."	
		foodOnHand['rice'] -= 2
		foodOnHand['nori'] -= 1
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_nori)
		leftClick()
		time.sleep(.1)
		foldMat()
		print "Done!"
		time.sleep(0.5)
		
		
	elif food == 'gunkan':
		print "Making a Gunkan..."
		foodOnHand['rice'] -= 1
		foodOnHand['nori'] -= 1
		foodOnHand['roe' ] -= 2	
		mousePos(Cord.f_rice)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_nori)
		leftClick()
		time.sleep(.05)
		mousePos(Cord.f_roe)
		leftClick()
		time.sleep(.1)
		mousePos(Cord.f_roe)
		leftClick()
		time.sleep(.1)
		foldMat()
		print "Done!"
		time.sleep(1.5)
		
def get_ready():
	box = (X_PAD + 976 , Y_PAD + 477 , X_PAD + 976 + 66 , Y_PAD + 477 + 58 )
	im = (ImageGrab.grab(box))
	#a = array(im.getcolors())
	#a = a.sum()
	im.save(CWD + "\\rice__" + str(int(time.time())) +	'.png', "PNG")
	#print a
	
def garbageCollection():
	print "Collecting garbage..."
	mousePos((X_PAD+365,Y_PAD+347))
	leftClick()
	time.sleep(.04)
	leftClick()
	leftClick()
	leftClick()
	time.sleep(.04)
    
    
    			
def foldMat():
	mousePos((Cord.f_rice[0]+40, Cord.f_rice[1]))
	leftClick()
	time.sleep(.1)
	
#-------------End Make Food---------------#

#----------- Buy Food ------------#
def buyFood(food):
	
	print "Buying food..."
	if food == 'rice':
		mousePos(Cord.phone)
		leftClick()
		time.sleep(.5)
		mousePos(Cord.menu_rice)
		leftClick()
		#box = (X_PAD + 976 , Y_PAD + 477 , X_PAD + 976 + 66 , Y_PAD + 477 + 58 )
		#im = ImageOps.grayscale(ImageGrab.grab(box))
		#a = array(im.getcolors())
		#s = a.sum()
		s = screenGrab()
		if s.getpixel(Cord.buy_rice) != (157, 53, 35):
			print "Rice is available."
			mousePos(Cord.buy_rice)
			time.sleep(.1)
			leftClick()
			mousePos(Cord.delivery_norm)
			time.sleep(.1)
			leftClick()
			foodOnHand['rice'] += 10
			time.sleep(2.5)
		else:
			print "Rice is not available, will wait."
			mousePos(Cord.t_exit)
			leftClick()
			time.sleep(1)
			buyFood(food)
	
	elif food == 'nori':
		mousePos(Cord.phone)
		leftClick()
		time.sleep(.2)
		mousePos(Cord.menu_toppings)
		time.sleep(.05)
		leftClick()
		s = screenGrab()
		time.sleep(.2)
		if s.getpixel(Cord.t_nori) != (53,53,39):
			print "Nori is available"
			mousePos(Cord.t_nori)
			leftClick()
			mousePos(Cord.delivery_norm)
			time.sleep(.2)
			leftClick()
			foodOnHand['nori'] += 7
			time.sleep(2.5)
		else:
			print "Nori is not available! :("
			mousePos(Cord.t_exit)
			leftClick()
			time.sleep(1)
			buyFood(food)
	
	elif food == 'shrimp':
		mousePos(Cord.phone)
		time.sleep(.2)
		leftClick()
		mousePos(Cord.menu_toppings)
		time.sleep(.2)
		leftClick()
		s = screenGrab()
		time.sleep(.2)
		if s.getpixel(Cord.t_shrimp) != (127,71,47):
			print "Shrimp is available!"
			mousePos(Cord.t_shrimp)
			leftClick()
			time.sleep(.2)
			mousePos(Cord.delivery_norm)
			leftClick()
			time.sleep(2.5)
		else:
			print "Shrimp is not available! :("
			mousePos(Cord.t_exit)
			leftClick()
			time.sleep(1)
			buyFood(food)
	
		
	elif food == 'roe':
		mousePos(Cord.phone)
		time.sleep(.2)
		leftClick()
		mousePos(Cord.menu_toppings)
		time.sleep(.2)
		leftClick()
		s = screenGrab()
		time.sleep(.2)
		if s.getpixel(Cord.t_roe) != (127,103,0):
			print "Fish eggs is available!"
			mousePos(Cord.t_roe)
			leftClick()
			time.sleep(.2)
			mousePos(Cord.delivery_norm)
			leftClick()
			foodOnHand['roe'] += 8
			time.sleep(2.5)
		else:
			print "Fish eggs are not available! :("
			mousePos(Cord.t_exit)
			leftClick()
			time.sleep(1)
			buyFood(food)
		
	elif food == 'salmon':
		mousePos(Cord.phone)
		time.sleep(.2)
		leftClick()
		mousePos(Cord.menu_toppings)
		time.sleep(.2)
		leftClick()
		s = screenGrab()
		time.sleep(.2)
		if s.getpixel(Cord.t_salmon) != (127,71,47):
			print "Salmon is available!"
			mousePos(Cord.t_salmon)
			leftClick()
			time.sleep(.2)
			mousePos(Cord.delivery_norm)
			leftClick()
			time.sleep(2.5)
		else:
			print "Salmon is not available! :("
			mousePos(Cord.t_exit)
			leftClick()
			time.sleep(1)
			buyFood(food)
		
	elif food == 'unagi':
		mousePos(Cord.phone)
		time.sleep(.2)
		leftClick()
		mousePos(Cord.menu_toppings)
		time.sleep(.2)
		leftClick()
		s = screenGrab()
		time.sleep(.2)
		if s.getpixel(Cord.t_unagi) != (123,85,51):
			print "Unagi is available!"
			mousePos(Cord.t_unagi)
			leftClick()
			time.sleep(.2)
			mousePos(Cord.delivery_norm)
			leftClick()
			time.sleep(2.5)
		else:
			print "Unagi is not available! :("
			mousePos(Cord.t_exit)
			leftClick()
			time.sleep(1)
			buyFood(food)	
	
	
def checkFood():
	print "Checking food supply..."
	for i, j in foodOnHand.items():
		if i == 'nori' or i == 'rice' or i == 'roe':
			if j <= 4:
				print "%s is low and needs to be replenished." % i
				buyFood(i)

#------------ End Buy Food ------------#


##########################
#   Check For Customer   #
##########################

def get_seat_one():
	box = (X_PAD +26, Y_PAD + 61, X_PAD + 26 + 63, Y_PAD + 61 + 16)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	#print a
	#im.save(CWD + "\\seat_one__" + str(int(time.time())) +	'.png', "PNG")	
	return a	
	
def get_seat_two():
	box = (X_PAD + 127,Y_PAD +61, X_PAD + 127 + 63, Y_PAD + 61 + 16)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	#print a
	#im.save(CWD + "\\seat_two__" + str(int(time.time())) +	'.png', "PNG")	
	return a
	
def get_seat_three():
	box = (X_PAD + 228, Y_PAD + 61, X_PAD + 228 + 63, Y_PAD + 61 + 16)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	#print a
	#im.save(CWD + "\\seat_three__" + str(int(time.time())) +	'.png', "PNG")	
	return a
	
def get_seat_four():
	box = (X_PAD + 329, Y_PAD + 61, X_PAD + 329 + 63, Y_PAD + 61 + 16)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	#print a
	#im.save(CWD + "\\seat_four__" + str(int(time.time())) +	'.png', "PNG")	
	return a
	
def get_seat_five():
	box = (X_PAD + 430, Y_PAD + 61, X_PAD + 430 + 63, Y_PAD + 61 + 16)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	#print a
	#im.save(CWD + "\\seat_five__" + str(int(time.time())) +	'.png', "PNG")	
	return a
	
def get_seat_six():
	box = (X_PAD + 531, Y_PAD + 61, X_PAD + 531+63, Y_PAD + 61 + 16)
	im = ImageOps.grayscale(ImageGrab.grab(box))
	a = array(im.getcolors())
	a = a.sum()
	#print a
	#im.save(CWD + "\\seat_six__" + str(int(time.time())) +	'.png', "PNG")	
	return a	
	
def get_all_seats():
	get_seat_six()
	get_seat_five()
	get_seat_four()
	get_seat_three()
	get_seat_two()
	get_seat_one() 
	

def clear_tables():
	print "Clearing tables...."
	mousePos((90, 204))
	leftClick()
	
	mousePos((191,202))
	leftClick()
	
	mousePos((291,203))
	leftClick()
	
	mousePos((389,202))
	leftClick()
	
	mousePos((493,202))
	leftClick()
	
	mousePos((595,201))
	leftClick()
	time.sleep(1)
	print "Done!"

def check_bubs(): #This is where the magic happens aka the main logic for the game.
	
	
	checkFood()
	s1 = get_seat_one()
	if s1 != Blank.seat_1:
		if sushiTypes.has_key(s1):
			print "Table 1 is occupied and needs %s" % sushiTypes[s1]
		else:
			print 'Sushi not found!'
	else:
		print 'Table 1 is unoccupied.'
		
	clear_tables()
	garbageCollection()
	checkFood()
	
	s2 = get_seat_two()
	if s2 != Blank.seat_2:
		if sushiTypes.has_key(s2):
			print 'Table 2 is occupied and needs %s' % sushiTypes[s2]
			makeFood(sushiTypes[s2])
		else:
			print "Sushi not found!"
	else:
		print "Table 2 is unoccupied."
	
	checkFood()
	
	
	s3 = get_seat_three()
	if s3 != Blank.seat_3:
		if sushiTypes.has_key(s3):
			print "Table 3 is occupied and needs %s" % sushiTypes[s3]
			makeFood(sushiTypes[s3])
		else:
			print "Sushi not found!"
	else:
		print "Table 3 is unoccupied."
		
	checkFood()
	
	s4 = get_seat_four()
	if s4 != Blank.seat_4:
		if sushiTypes.has_key(s4):
			print "Table 4 is occupied and needs %s" % sushiTypes[s4]
			makeFood(sushiTypes[s4])
		else:
			print "Sushi not found!"
	else:
		print "Table 4 is unoccupied."
		
	
	clear_tables()
	garbageCollection()
	checkFood()
	
	s5 = get_seat_five()
	if s5 != Blank.seat_5:
		if sushiTypes.has_key(s5):
			print "Table 5 is unoccupid and needs %s" % sushiTypes[s5]
			makeFood(sushiTypes[s5])
		else:
			print "sushi not found!"
	else:
		print "Table 5 is not currently occupied."
		
	
	checkFood()
	
	s6 = get_seat_six()
	if s6 != Blank.seat_6:
		if sushiTypes.has_key(s6):
			print "Table 6 is occupied and needs %s" % sushiTypes[s6]
			makeFood(sushiTypes[s6])
		else:
			print "Sushi type not found!"
	else:
		print "Table 6 is not currently occupied."
		
		
	clear_tables()
	garbageCollection()
#-------------End Functions---------------#
	
def main():
	banner()
	start_game()
	while True:
		check_bubs()
	
	
	
	
if __name__ == '__main__':
	main()
