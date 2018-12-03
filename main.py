import subprocess
from math import *
import numpy as np

# Import custom libs
from utils import *

# Get image
#subprocess.call("gen_image.sh", shell=True)


# Parameters

WIDTH_Conv_1 = 24
HEIGHT_Conv_1 = 24

WIDTH_Max_1 = 12
HEIGHT_Max_1 = 12

WIDTH_Conv_2 = 12
HEIGHT_Conv_2 = 12

WIDTH_Max_2 = 6
HEIGHT_Max_2 = 6

WIDTH_Conv_3 = 6
HEIGHT_Conv_3 = 6

WIDTH_Max_3 = 3
HEIGHT_Max_3 = 3

#------ Convolution matrix ----------------------------------------------------------------------------------------------------------

# First Convolution Matrix 3X3X3
H = np.array([[[1,2,3],[1,2,3],[1,2,3]],[[1,2,3],[1,2,3],[1,2,3]],[[1,2,3],[1,2,3],[1,2,3]]])

H_l = []
H_l.append( H )
H_l.append( H )
H_l.append( H )
H_l.append( H ) # H_l = (3X3X3)x4

# Second Convolution Matrix 3x3x4
H2 = np.array([[[4,5,6,7],[4,5,6,7],[4,5,6,7]],[[4,5,6,7],[4,5,6,7],[4,5,6,7]],[[4,5,6,7],[4,5,6,7],[4,5,6,7]]]) 

H_l2 = []
H_l2.append( H2 )
H_l2.append( H2 )#H_l2 = (3X3X4)x2

# Third Convolution Matrix 3x3x2
H3 = np.array([[[4,5],[4,5],[4,5]],[[4,5],[4,5],[4,5]],[[4,5],[4,5],[4,5]]])

H_l3 = []
H_l3.append( H3 )
H_l3.append( H3 )
H_l3.append( H3 )
H_l3.append( H3 )
H_l3.append( H3 ) #H_l = (3X3X2)x5

#------ Perceptron Matrix ----------------------------------------------------------------------------------------------------------

Perceptron_Matrix = np.array([[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5],[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,1,2,3,4,5] ])

# Options :
np.set_printoptions(threshold=np.nan)

# Init variables
Header = []
tab_line = ''
width = 0
height = 0
total_elements = 0
cnt = 0

#------ Functions def  ----------------------------------------------------------------------------------------------------------

def convolution(img, H_list, WIDTH, HEIGHT):
	"""
	Input : Image to convolute, number of channels in the output, H matrices
	Output : Image with size width*height*channels 
	"""
	img_out = np.zeros((WIDTH,HEIGHT,len(H_list)), np.float32) # H_list = number of channels

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
			img = np.insert(img, 0, 0, axis=0)
			img = np.insert(img, WIDTH+1, 0, axis=0) # +1 because you aim a new inexisting line

		for j in range( 0, from_j ):
			img = np.insert(img, 0, 0, axis=1)
			img = np.insert(img, HEIGHT+1, 0, axis=1)

		for i in range( from_i, to_i):
			for j in range( from_j, to_j):
				(width_H, height_H, colors) = H.shape
				img_out[i-from_i][j-from_j][counter] = np.sum(np.multiply(img[i-from_i:i+from_i+1, j-from_j:j+from_j+1] , H ))

		counter +=1

	return img_out 
	

#------ Get Image ----------------------------------------------------------------------------------------------------------

def relu(img):

	(width, height, channel) = img.shape
	img_out = np.zeros((width,height,channel), np.float32)
	
	bias = np.zeros(channel, np.float32)
	
	for k in range( 0, channel):
		for i in range( 0, width):
    			for j in range( 0, height):
				img_out[i,j,k] = img[i][j][k] + bias[k]
			if (img_out[i][j][k] < 0):
				img_out[i,j,k] = 0
					
	return img_out

#------ Max Pool ----------------------------------------------------------------------------------------------------------

def Max_Pool(img,WIDTH,HEIGHT):

	img_reshaped = np.insert(img, 0, 0, axis=0)#adding a ligne of zeros
			
	img_reshaped = np.insert(img_reshaped, 0, 0, axis=1)#adding a column of zeros
	
	(width, height, channel) = img_reshaped.shape
			
	img_out = np.zeros((WIDTH, HEIGHT, channel), np.float32)

	from_i = 0
	from_j = 0
	
	for k in range( 0, channel):
		for i in range( 0, WIDTH):
    			for j in range( 0, HEIGHT):
				img_out[i,j,k] = Max_Matrix(img_reshaped[from_i:from_i+3,from_j:from_j+3,k])
				from_j = from_j + 2			
			from_j = 0 
			from_i = from_i + 2
        	from_i = 0
				
	return img_out

#------ Max Pool's auxiliar function ---------------------------------------------------------------------------------------------------

def Max_Matrix(img):
	
	max_value = 0
 	
	for i in range( 0, 3):
		for j in range( 0, 3):
			if( img[i][j]> max_value):			
				max_value = img[i][j] 
			
	return max_value; 


#------ Fully Connected (Perceptron) ---------------------------------------------------------------------------------------------------

def Perceptron(img):

	(width) = img.shape
	
	Perceptron_img = np.zeros(width,np.float32)

	Perceptron_img = np.multiply(img,Perceptron_Matrix)

	return Perceptron_img




#------ Get Image ---------------------------------------------------------------------------------------------------------------------

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
				

# --- Image Resizing to 24 x 24 and normalizing ---

Image = cut_image(Image, WIDTH_Conv_1, HEIGHT_Conv_1)
Image = normalize(Image)

# ------ Convolution -------------------------------------------------------------------------------------------------------------------

print("Before First conv");

img_conv_1 = convolution(Image, H_l, WIDTH_Conv_1, HEIGHT_Conv_1)

print("After First conv");


# ----- RELU ---------------------------------------------------------------------------------------------------------------------

print("Before first RELU");

img_relu_1 = relu(img_conv_1);

print("After first conv");


# ----- Max_Pool -----------------------------------------------------------------------------------------------------------------
print("Before Max Pool");

img_max_pool_1 = Max_Pool(img_relu_1, WIDTH_Max_1, HEIGHT_Max_1)

print("After Max Pool");


# ----- Second convolution -------------------------------------------------------------------------------------------------------
print("Before second conv");

img_conv_2 = convolution(img_max_pool_1, H_l2, WIDTH_Conv_2, HEIGHT_Conv_2)

print("After second conv");

# ----- Second Max_Pool ----------------------------------------------------------------------------------------------------------
print("Before 2 Max Pool");

img_max_pool_2 = Max_Pool(img_conv_2, WIDTH_Max_2, HEIGHT_Max_2)

print("After 2 Max Pool");

# ----- Third convolution -------------------------------------------------------------------------------------------------------------
print("Before third conv");

img_conv_3 = convolution(img_max_pool_2, H_l3, WIDTH_Conv_3, HEIGHT_Conv_3)

print("After third conv");

# ----- Third Max_Pool -------------------------------------------------------------------------------------------------------------
print("Before 3 Max Pool");

img_max_pool_3 = Max_Pool(img_conv_3, WIDTH_Max_3, HEIGHT_Max_3)

print("After 3 Max Pool");

# ----- Reshape -----------------------------------------------------------------------------------------------------------------
print("Before Reshape");

(width, height, channel) = img_max_pool_3.shape

img_reshape = np.reshape(img_max_pool_3, width*height*channel)

# ----- Perceptron ---------------------------------------------------------------------------------------------------------------------
print("Before Perceptron");

img_perceptron = Perceptron(img_reshape)

print("After Perceptron");

