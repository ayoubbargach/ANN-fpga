"""
 
    The purpose of this file
    ----------------------
 
    Get the matrices from the CNN txt file 
 
 
"""
import numpy as np

# Add a function to format white spaces
def clean(text):
	text = ' '.join(text.split()) # remove all multiple spaces
	text = text.replace(" [", "[")
	text = text.replace(" ]", "]")
	text = text.replace("[ ", "[")
	text = text.replace("] ", "]")

	return text
	
	
# Recursive function to format
def recursive_array(text, i=0):
	if (len(text) < i):
		return None, i
	elif text[i] == '[':

		#Increment i to avoid char '['
		i += 1

		# Before doing more complicated stuff, let us analyse the following char to predict the behavior

		if text[i].isdigit() or text[i] == '-':
			return recursive_array(text, i)
		
		else :
			# We open a new context
			context = []

			while (True):
				element = recursive_array(text, i)

				# Lets save now the new i for the potentiel next iteration 
				i = element[1]

				if (element[0] == None):
					# Then we have to close the context
					return context, i
				else :
					context.append(element[0])

	elif text[i].isdigit() or text[i] == '-':
		# We start by locating the next ]
		end = text.index(']', i)

		# Then we split by using the indexes and the parameter whitespace
		result = text[i:end].split(" ")

		# We convert each element and return it as a list of floats
		return [float(e) for e in result], end+1
	
	else :
		return None, i+1

def get_new_config_format(config):
	""" Function that analyze the previous extraction so it can suits our needs
	"""
	


	# Each conv

	config["conv1/weights"] = [ np.array([[[config["conv1/weights"][0][i][j][k][channel] for k in range(0, 3)] for j in range(0, 3)] for i in range(0, 3)]) for channel in range(0,64)]
	config["conv2/weights"] = [ np.array([[[config["conv2/weights"][0][i][j][k][channel] for k in range(0, 64)] for j in range(0, 3)] for i in range(0, 3)]) for channel in range(0,32)]
	config["conv3/weights"] = [ np.array([[[config["conv3/weights"][0][i][j][k][channel] for k in range(0, 32)] for j in range(0, 3)] for i in range(0, 3)]) for channel in range(0,20)]

	# Perceptron
	config["local3/weights"] = np.array(config["local3/weights"][0]) # 2D array no need to add more information

	# Bias management
	config["conv1/biases"] = np.array(config["conv1/biases"][0])
	config["conv2/biases"] = np.array(config["conv2/biases"][0])
	config["conv3/biases"] = np.array(config["conv3/biases"][0])
	config["local3/biases"] = np.array(config["local3/biases"][0])

	"""
	# print for channel 0

	new_conf = [[[tmp[0][i][j][k][0] for k in range(0, 3)] for j in range(0, 3)] for i in range(0, 3)]

	print(new_conf)"""


	return config



def get_config(filename):
	""" Returns an array formatted from the filename issued	"""

	key = ""
	content = {} # We create a dictionary to keep track of all informations

	with open(filename) as txt:
		for line in txt:
			# we start by testing if we are in case of an array :
			if line.startswith("tensor_name:") :
				# OK, we are at the start of an array, lets get all the lines
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
			
			content[key] = recursive_array(clean(value))

	return get_new_config_format(content)
			
