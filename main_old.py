import subprocess
from math import *
import numpy as np

# Import custom libs
from utils import *

# Get image
subprocess.call("gen_image.sh", shell=True)

# PARAMETERS -- MODIFY HERE

# Initial size image
WIDTH = 24
HEIGHT = 24

# Convolution matrix
H=np.array([[[1,2,3],[1,2,3],[1,2,3]], [[1,2,3],[1,2,3],[1,2,3]], [[1,2,3],[1,2,3],[1,2,3]]])

H_l = []
H_l.append( H )
H_l.append( H )


# Options :
np.set_printoptions(threshold=np.nan)

# Init variables
Header = []
tab_line = ''
width = 0
height = 0
total_elements = 0
cnt = 0

# --- Functions def ---


def convolution(Image, H_list):
	"""
	Input : Image to convolute, number of channels in the output, H matrices
	Output : Image with size width*height*channels 
	"""
	Res_Image = np.zeros((WIDTH,HEIGHT,len(H_list)), np.float32) #H_list = number of channels

	print(H_list[0] )

	(width_H, height_H, colors) = H_list[0].shape

	

	counter = 0
	
	for H in H_list: # nombre de canaux

		# Loop parameters

		from_i = width_H % 2
		to_i = WIDTH + from_i

		from_j = height_H % 2
		to_j = HEIGHT + from_j

		# Add some padding to the initial image

		for i in range( 0, from_i ):
			Image = np.insert(Image, 0, 0, axis=0)
			Image = np.insert(Image, WIDTH+1, 0, axis=0) # +1 because you aim a new inexisting line

		for j in range( 0, from_j ):
			Image = np.insert(Image, 0, 0, axis=1)
			Image = np.insert(Image, HEIGHT+1, 0, axis=1)

		for i in range( from_i, to_i):
			for j in range( from_j, to_j):
				# attention il faut changer le H lors qu'on travaille avec plusieurs canaux :
				Res_Image[i-from_i][j-from_j][counter] = np.sum( np.multiply( Image[i-from_i:i+from_i+1, j-from_j:j+from_j+1] , H ))

		counter +=1

	return Res_Image 
	

# --- Get Image ---
"""
def relu(Image, H_list):
	Res_Image = np.zeros((WIDTH,HEIGHT,H_list.shape), np.float32) #H_list = number of channels
	
	for H in H_list: # nombre de canaux	
		for i in range( 0, WIDTH):
 	    		for j in range( 0, HEIGHT):
				for k in range(0,3):
					Res_Image[i][j][counter]	


	return e_x """

# --- Get Image ---

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
					
				Image[i,j,k] = int(tab_line[cnt]) # Convert ASCII to int
				cnt+=1
				
			

	# print (Image)
	# The Image tab is ready, we can close the file

# --- Image Resizing to 24 x 24 and normalizing ---

Image = cut_image(Image, WIDTH, HEIGHT)
Image = normalize(Image)

# --- Convolution and pooling part ---
# http://www.f-legrand.fr/scidoc/docimg/image/filtrage/convolution/convolution.html

Res_Image = convolution(Image, H_l)

print(Res_Image)

# The MAIN function 

def main(argv):             
    image = "image.ppm"      
    try:              
        opts, args = getopt.getopt(argv, "hi:d", ["help", "image="])
    except getopt.GetoptError: 
        usage()           
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()  
            sys.exit()
        elif opt == '-d':
            global _debug
            _debug = 1                  
        elif opt in ("-i", "--image"): 
            image = arg               

    # some additionnal logic 

if __name__ == "__main__":
    # execute only if run as a script
    main()
