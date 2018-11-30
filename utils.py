from math import *
import numpy as np

""" utils.py is dedicated to utils functions, you can find the following functions :
 """


def get_line( image ):
	line = image.readline()
	line = line.replace('\n', '').split(' ')
	return line

def cut_image( image, aimed_width, aimed_height ):
	(width, height, depth) = image.shape
	offset_width = 0
	offset_height = 0
	
	new_Image = np.zeros((aimed_width, aimed_height, 3), np.uint8)

	if (width >= aimed_width and height >= aimed_height):
		offset_width = (width - aimed_width) // 2	
		offset_height = (height - aimed_height) // 2

		for j in range(offset_height, offset_height+aimed_width):
			for i in range(offset_width, offset_width+aimed_height):
				new_Image[i-offset_height][j-offset_width] = image[i][j]
	else :
		print('WARNING : The initial image is too small for the aimed resizing.');
	
	return new_Image

def normalize( matrix ):
	(width, height,depth) = matrix.shape

	mean = 0
	variance = 0
	size = width * height * depth

	# compute mean 
	for k in range(0, depth):
		for i in range(0, width):
			for j in range(0, height):
				mean += matrix[i][j][k]
	mean /= size
	
	# compute variance
	for k in range(0, depth):
		for i in range(0, width):
			for j in range(0, height):
				variance += (matrix[i][j][k] - mean)**2

	variance /= size
	variance = sqrt( variance )

	new_matrix = np.zeros((width, height,depth), np.float32)
	for k in range(0, depth):
		for i in range(0, width):
			for j in range(0, height):
				new_matrix[i][j][k] = (matrix[i][j][k] - mean) / max( variance, 1/sqrt(size)) 
	
	return new_matrix 

def softmax(x):
	"""Compute softmax values for each sets of scores in x."""
	e_x = np.exp(x - np.max(x))
	return e_x / e_x.sum(axis=0)


