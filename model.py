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

def model(Image, conf, target):
	
	# Intro
	print("\n ------- /!\ ANN-fpga STEP /!\ -------  :\n")

	#------ Convolution matrix ----------------------------------------------------------------------------------------------------------


	# First Convolution Matrix 3X3X3

	H_l = conf["conv1/weights"]
	B1 = conf["conv1/biases"]


	# Second Convolution Matrix 3x3x4

	H_l2 = conf["conv2/weights"]
	B2 = conf["conv2/biases"]

	# Third Convolution Matrix 3x3x2

	H_l3 = conf["conv3/weights"]
	B3 = conf["conv3/biases"]

	# Perceptron

	H_l4 = conf["local3/weights"]
	B4 = conf["local3/biases"]



    # --- Image Resizing to 24 x 24 and normalizing ---

	Image = cut_image(Image, WIDTH_Conv_1, HEIGHT_Conv_1)
	Image = normalize(Image)

	# ------ Convolution -------------------------------------------------------------------------------------------------------------------

	print("> First conv")

	img_conv_1 = convolution(Image, H_l, WIDTH_Conv_1, HEIGHT_Conv_1)



	# ----- RELU ---------------------------------------------------------------------------------------------------------------------

	print("> First RELU")

	img_relu_1 = relu(img_conv_1, B1)



	# ----- Max_Pool -----------------------------------------------------------------------------------------------------------------
	print("> Max Pool")

	img_max_pool_1 = Max_Pool(img_relu_1, WIDTH_Max_1, HEIGHT_Max_1)



	# ----- Second convolution -------------------------------------------------------------------------------------------------------
	print("> Before second conv")

	img_conv_2 = convolution(img_max_pool_1, H_l2, WIDTH_Conv_2, HEIGHT_Conv_2)


	# ----- RELU ---------------------------------------------------------------------------------------------------------------------

	print("> Before second RELU")

	img_relu_2 = relu(img_conv_2, B2)


	# ----- Second Max_Pool ----------------------------------------------------------------------------------------------------------
	print("> Before 2 Max Pool")

	img_max_pool_2 = Max_Pool(img_conv_2, WIDTH_Max_2, HEIGHT_Max_2)


	# ----- Third convolution -------------------------------------------------------------------------------------------------------------
	print("> Before third conv")

	img_conv_3 = convolution(img_max_pool_2, H_l3, WIDTH_Conv_3, HEIGHT_Conv_3)

	
	# ----- RELU ---------------------------------------------------------------------------------------------------------------------

	print("> Before third RELU")

	img_relu_3 = relu(img_conv_3, B3)


	# ----- Third Max_Pool -------------------------------------------------------------------------------------------------------------
	print("> Before 3 Max Pool")

	img_max_pool_3 = Max_Pool(img_relu_3, WIDTH_Max_3, HEIGHT_Max_3)


	# ----- Reshape -----------------------------------------------------------------------------------------------------------------
	print("> Reshape")

	(width, height, channel) = img_max_pool_3.shape

	img_reshape = np.reshape(img_max_pool_3, width*height*channel, order='C')

	# ----- Perceptron ---------------------------------------------------------------------------------------------------------------------
	print("> Perceptron")

	img_perceptron = Perceptron(H_l4, img_reshape, B4)

	# ----- Softmax and inference ---------------------------------------------------------------------------------------------------------------------
	print("> Softmax and inference")

	img_final = softmax(img_perceptron)


	classes = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

	pos = np.argmax(img_final)

	# Get the class :

	print("The class is : " + classes[pos])

	if (target == pos):
		print("Target is reached ! Nice job.")
	else :
		print("Not accurate, because target is : "+classes[target]+"." )


	












