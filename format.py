from math import *
import numpy as np
import ast

		
	
filename = "CNN_coeff_3x3.txt"

def get_array(filename):
	""" Returns an array formatted from the filename issued	"""

	output_array = []
	key = ""
	content = {} # We create a dictionary to keep track of all informations

	with open(filename) as txt:
		for line in txt:
			# we start by testing if we are in case of an array :
			if line.startswith("tensor_name:") :
				# OK, we are at the start of an array, lets get all the lines
				print("We analyse the "+line)
				# We add a new key value, key = line - { tensor_name } and value empty ""
				key = line.replace("tensor_name:", "").strip()
				content[key] = ""
			else :
				# Conactenate all the line (all the \n are deleted with strip() )
				content[key] += line.strip()
				# Add space
				content[key] += " "

		# let us loop again in each key and generate an array for each of them
		# Note that we simply replace the raw data with the generated array
		for key, value in content.iteritems() :
    			print("Generating an array for the key " + key)
			value = ast.literal_eval(value)
			print value
			
		


get_array(filename)
