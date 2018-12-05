"""
 
    The purpose of this file
    ----------------------
 
    test
 
 
"""


from lib import *


# Parameters

CNN_model = "CNN_coeff_3x3.txt"

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

def model(Image, conf):

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

    # --- Image Resizing to 24 x 24 and normalizing ---

	Image = cut_image(Image, WIDTH_Conv_1, HEIGHT_Conv_1)
	Image = normalize(Image)

	# ------ Convolution -------------------------------------------------------------------------------------------------------------------

	print("Before First conv")

	img_conv_1 = convolution(Image, H_l, WIDTH_Conv_1, HEIGHT_Conv_1)

	print("After First conv")


	# ----- RELU ---------------------------------------------------------------------------------------------------------------------

	print("Before first RELU")

	img_relu_1 = relu(img_conv_1)

	print("After first conv")


	# ----- Max_Pool -----------------------------------------------------------------------------------------------------------------
	print("Before Max Pool")

	img_max_pool_1 = Max_Pool(img_relu_1, WIDTH_Max_1, HEIGHT_Max_1)

	print("After Max Pool")


	# ----- Second convolution -------------------------------------------------------------------------------------------------------
	print("Before second conv")

	img_conv_2 = convolution(img_max_pool_1, H_l2, WIDTH_Conv_2, HEIGHT_Conv_2)

	print("After second conv")

	# ----- Second Max_Pool ----------------------------------------------------------------------------------------------------------
	print("Before 2 Max Pool")

	img_max_pool_2 = Max_Pool(img_conv_2, WIDTH_Max_2, HEIGHT_Max_2)

	print("After 2 Max Pool")

	# ----- Third convolution -------------------------------------------------------------------------------------------------------------
	print("Before third conv")

	img_conv_3 = convolution(img_max_pool_2, H_l3, WIDTH_Conv_3, HEIGHT_Conv_3)

	print("After third conv")

	# ----- Third Max_Pool -------------------------------------------------------------------------------------------------------------
	print("Before 3 Max Pool")

	img_max_pool_3 = Max_Pool(img_conv_3, WIDTH_Max_3, HEIGHT_Max_3)

	print("After 3 Max Pool")

	# ----- Reshape -----------------------------------------------------------------------------------------------------------------
	print("Before Reshape")

	(width, height, channel) = img_max_pool_3.shape

	img_reshape = np.reshape(img_max_pool_3, width*height*channel)

	# ----- Perceptron ---------------------------------------------------------------------------------------------------------------------
	print("Before Perceptron")

	img_perceptron = Perceptron(img_reshape)

	print("After Perceptron")