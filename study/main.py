#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
"""
    The ``ANN-fpga`` project
    ======================
 
    This project have been developed during studies in the engineering french school : Phelma Grenoble INP.
 
    The aim of the project
    ----------------------
 
    The aim of the project is to analyse all the flow, from the python protyping to the fpga implementation.
	I think that this script may be very usefull for a lot of people that are working on AI projects.
	Indeed, FPGA is the next step to have a better performance comparing to graphic cards.

	The implementation
    ------------------

	We implement here a simple CNN network to classify pictures, there is a specific size of image to follow !
 
 
"""

import subprocess
import os
import sys 
import getopt
import struct
import numpy as np

# Import custom libs
from utils import *
from model import *
from format import *

#------ /!\ MAIN FUNCTIONS /!\ ----------------------------------------------------------------------------------------------------------------

""" Print how to use the program"""
def usage():
	print(""" CNN program example - Help panel :
	(*) Use -h or --help to print the help.
	(*) Use -i or --image to set a new raw image to work on. Default = image.raw
	(*) Use -s or --steps to set the number of small colored pictures of 32*32 pixel to extract from your raw image.
		So the offset between each image should be 3072 bytes. Default = 1

		If the parameter -s is set to -1, the image accepted is a ppm image named image.ppm (same directory).
			
	Developed by Ayoub Bargach and Margareth Mee.
	""")

""" Main function, it get the raw image, then generate step by step the small images using the script gen_script.sh """
def main(argv):

	# Intro
	print("\n ------- /!\ ANN-fpga STARTING /!\ -------  :\n")
	
	# Options :
	np.set_printoptions(threshold=np.nan)
	fileDir = os.path.dirname(os.path.realpath('__file__'))

	
	image_name = "private/cifar-10-binary/cifar-10-batches-bin/test_batch.bin"
	flag_jump_img_gen = False
	steps = 1
	target = 0

	try:              
		opts, args = getopt.getopt(argv, "hi:s:", ["help", "image=", "steps="])
	except getopt.GetoptError: 
		usage()           
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()  
			sys.exit()              
		elif opt in ("-i", "--image"): 
			image_name = arg
		elif opt in ("-s", "--steps"): 
			steps = int(arg)

	
	if (steps == -1) :
		steps = 1
		flag_jump_img_gen = True

	if not flag_jump_img_gen :
		# Lets set an evironment variable to be used by the bash script
		os.environ['PHELMA_ANN_PROJECT_IMAGE_RAW'] = image_name
		


	# Before going further, lets generate the model weights and biases (dictionary)
	model_config = get_config(CNN_model)
	stats = []

	for i in range(0, steps):
		if not flag_jump_img_gen:
			# Get image	
			os.environ['PHELMA_ANN_PROJECT_OFFSET'] = str(i * 3073 + 1)
			os.environ['PHELMA_ANN_PROJECT_STEP'] = str(i * 3073)

			# The bash script generate an image named image.ppm
			subprocess.call("./gen_image.sh", shell=True)
			
			
			
			with open("class.raw", "rb") as file_temp :

				data = file_temp.read()
				target = struct.unpack('>i', data)[0]

				target = target >> 24 # We want only the first 8 bits
				



		# For each image, we want to generate an array to be manipulated by the model
		image = get_image("image.ppm")

		print("\n ------- /!\ ANN-fpga STEP "+ str(i) +" /!\ -------  :\n")
		# Then lets apply the model on this image and add the stats
		stats.append( model(image, model_config, target) )

	accuracy = 0.0

	# print the accuracy
	for i in range( 0, len(stats)):
		accuracy += stats[i][2]
	
	accuracy /= len(stats)

	print("The accuracy for " + str(steps) + " steps : " + str(accuracy*100) + " %.")



"""Is executed only if we are running this script (not by importing it)"""
if __name__ == "__main__":
    
    main(sys.argv[1:])




