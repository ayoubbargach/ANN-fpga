
# Add a function to format white spaces

	
# Recursive function to format
def recurs_array(text, i = 0):
	if text[i] == '[':
		
		result = []
		counter = 0
		i += 1
		print (i)
		while (True) :
			tmp = recurs_array(text, i)
			print(tmp)
			if  tmp[0] == None :
				if counter == 1 :
					print("HERE")
					return result[0], tmp[1]
				else :
					return result, tmp[1]
			else :
				counter += 1
				result.append(tmp[0])
				i = tmp[1]

	elif text[i] == ']' :
		return None, i+1
	elif text[i].isdigit():
		# We start by locating the next ]
		end = text.index(']', i)

		# Then we split by using the indexes and the parameter whitespace
		result = text[i:end].split(" ")
		return result, end
	else :
		return None, i
	

	
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
			# value = ast.literal_eval(value)
			print value
			
		

test_list = "[[1 0][[1 0][2 3]]]"

print("GO")

r =recurs_array(test_list)

print ("GO")
print(r)
