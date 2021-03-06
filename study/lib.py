"""
 
    The purpose of this file
    ----------------------
 
    test
 
 
"""


import numpy as np
from math import sqrt


#------ Resize image ---------------------------------------------------------------------------------------------------


def cut_image( image, aimed_width, aimed_height ):
	(width, height, depth) = image.shape
	offset_width = 0
	offset_height = 0
	
	new_Image = np.zeros((aimed_width, aimed_height, 3), np.float32)

	if (width >= aimed_width and height >= aimed_height):
		offset_width = (width - aimed_width) // 2	
		offset_height = (height - aimed_height) // 2

		for j in range(offset_height, offset_height+aimed_width):
			for i in range(offset_width, offset_width+aimed_height):
				new_Image[i-offset_height][j-offset_width] = image[i][j]
	else :
		print('WARNING : The initial image is too small for the aimed resizing.')
	
	return new_Image

#------ Normalize ---------------------------------------------------------------------------------------------------


def normalize( matrix ):
	(width, height, depth) = matrix.shape

	mean = 0
	variance = 0
	size = width * height * depth

	# compute mean 
	for k in range(0, depth):
		for i in range(0, width):
			for j in range(0, height):
				mean += matrix[i,j,k]
	mean /= size
	
	# compute variance
	for k in range(0, depth):
		for i in range(0, width):
			for j in range(0, height):
				variance += (matrix[i,j,k] - mean)**2

	variance /= size
	variance = sqrt( variance )

	new_matrix = np.zeros((width, height,depth), np.float32)
	for k in range(0, depth):
		for i in range(0, width):
			for j in range(0, height):
				new_matrix[i,j,k] = (matrix[i,j,k] - mean) / max( variance, 1/sqrt(size)) 
	
	return new_matrix

#------ softmax function ---------------------------------------------------------------------------------------------------


def softmax(x):
	"""Compute softmax values for each sets of scores in x."""
	e_x = np.exp(x)
	return e_x /e_x.sum()



#------ Functions def  ----------------------------------------------------------------------------------------------------------

def convolution(img, H_list, WIDTH, HEIGHT): # 4x4x3  (3x3x3)x2  4 4
	"""
	Input : Image to convolute, number of channels in the output, H matrices
	Output : Image with size width*height*channels 
	"""
	img_out = np.zeros((WIDTH,HEIGHT,len(H_list)), np.float32) # H_list = number of channels

	(width_H, height_H, colors) = H_list[0].shape

	counter = 0
	max_k = colors-1  
	
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

	for H in H_list: # nombre de canaux

		sum_all = 0
		"""	
		for i in range( from_i, to_i):
			for j in range( from_j, to_j):
				for k in range( 0, colors):	
				
					sum_all += np.sum(np.multiply(img[i-from_i:i+from_i+1, j-from_j:j+from_j+1, k] , H[:,:,k] ))
					
					if(k == max_k):
						img_out[i-from_i,j-from_j,counter] = sum_all
						sum_all = 0 """
			
		for k in range( 0, colors):
			for i in range( from_i, to_i):
				for j in range( from_j, to_j):
					sum_all += np.sum(np.multiply(img[i-from_i:i+from_i+1, j-from_j:j+from_j+1, k] , H[:,:,k] ))

		img_out[i-from_i,j-from_j,counter] = sum_all
		sum_all = 0 

		counter +=1

	return img_out 
	

#------ Get Image ----------------------------------------------------------------------------------------------------------

def relu(img, bias):

	(width, height, channel) = img.shape
	img_out = np.zeros((width,height,channel), np.float32)
	
	
	for k in range( 0, channel):
		for i in range( 0, width):
    			for j in range( 0, height):
				img_out[i,j,k] = img[i,j,k] + bias[k]
				if (img_out[i,j,k] < 0):
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
			if( img[i,j]> max_value):			
				max_value = img[i,j] 
			
	return max_value


#------ Fully Connected (Perceptron) ---------------------------------------------------------------------------------------------------

def Perceptron(Perceptron_Matrix, img, bias):

	(width) = img.shape
	
	Perceptron_img = np.zeros(width,np.float32)

	Perceptron_img = np.dot(img,Perceptron_Matrix)

	Perceptron_img = Perceptron_img + bias

	return Perceptron_img

def Reshape(img):

	(width, height, channel) = img.shape
	
	img_out = np.zeros((width*height*channel), np.float32)

	index = 0
	
	for j in range( 0, height):
		for i in range( 0, width):
			for k in range( 0, channel):
				img_out[index] = img[i,j,k]
				index = index+1		

	return img_out





