
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

					
	

	
filename = "CNN_coeff_3x3.txt"

def get_array(filename):
	""" Returns an array formatted from the filename issued	"""

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
			
			value = recursive_array(clean(value))
			print(value)
			


	return content
			
		
content = get_array(filename)
