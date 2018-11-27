import ImageGrab
import os
import time 


'''
All cooridnates assume a 1920 x 1200 resolution, no toolbars, using firefox

x_pad = 464
y_pad = 224
play_area = x_pad + 1, y_pad + 1,  1104, 703
'''


########################
#   Global Variables   #
########################
'''
This defines any and all 'magic numbers' and the like. 

Note: All global variables will be written in CAPS for ease of use.

'''

CWD = os.getcwd() #This grabs the current working directory.
x_pad = 464
y_pad = 223

def screenGrab(): #This grabs a screenshot and saves in the current working directory as a '.png' file.
	box = ()
	im = ImageGrab.grab()
	im.save(CWD + '\\ful_snap__' + str(int(time.time())) + '.png', 'PNG') #(directory, (name, timestamp), fileformat)
	



def main():
	screenGrab()
	
	
if __name__ == '__main__':
	main()
