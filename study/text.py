import numpy as np

x = np.array([1.32, 2.36, 6.15, 7.80])

print(x.sum(axis=0))

print(x / x.sum(axis=0))
def softmax(x):
	"""Compute softmax values for each sets of scores in x."""
	e_x = np.exp(x )
	return e_x / e_x.sum()
