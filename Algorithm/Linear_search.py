def linear_search(list, target):


# return the index of the target value, else returns None



	for i in range(0, len(list)):
		if list[i] == target:
			return i
	return None

def verify(index):
	if index is not None:
		print("Target found at index: ", index)
	else: 
		print("Target not found inlist")






