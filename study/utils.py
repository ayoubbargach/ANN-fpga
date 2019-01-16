"""
 
    The purpose of this file
    ----------------------
 
    test
 
 
"""


import numpy as np


""" utils.py is dedicated to utils functions, you can find the following functions :
 """


def get_line( image ):
	line = image.readline()
	line = line.replace('\n', '').split(' ')
	return line

def get_image(filename):

	# Init
	Header = []
	tab_line = ""
	total_elements = 0
	cnt = 0

	with open('image.ppm') as img:
		# Header generation
		Header.append(img.readline())
		Header.append(img.readline())
		Header.append(img.readline())

		# Size generation
		Header[1] = Header[1].replace('\n', '').split(' ')
		width = int(Header[1][0])
		height = int(Header[1][1])
		
		Image = np.zeros((width,height,3), np.uint8)

		# Image generation : Keep in mind that the read line is maybe different to width of image
		for i in range(0, height):
			for j in range(0, width):
				for k in range(0, 3): # k is for RGB management. We need 3 values to code one color.
					if ( cnt == total_elements ):
						tab_line = get_line(img)
						total_elements = len(tab_line)
						cnt = 0
					if ( tab_line[cnt] == '' ):
						cnt += 1
						if ( cnt == total_elements ):
							tab_line = get_line(img)
							total_elements = len(tab_line)
							cnt = 0
						
					Image[i,j,k] = int(tab_line[cnt]) # Conv ASCII to int
					cnt+=1
	return Image



