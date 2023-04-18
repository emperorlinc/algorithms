import time
from functools import wraps

sorted_list = [0,1,2,3,4,5,6,7,8,9]
unsorted_list = [5,4,6,7,2,1,3,0,9,8]

def time_measurement(fn):
	@wraps(fn)
	def wrapper(*args, **kwargs):
		time_begin = time.time()
		fn(*args, **kwargs)
		time_end = time.time()
		print(f"Total Execution Time: {time_end - time_begin}")
		return fn(*args, **kwargs)
	return wrapper


@time_measurement
def linear_search(list, target):
	for x in list:
		if x == target:
			return x
	return target


@time_measurement
def binary_search(list, target):
	""" It uses the divide and conquer method to search for the target
	    It runs in Constant time - O(1)"""
	start = list[0]
	end = list[-1]

	while start <= end:
		midpoint = (start + end) // 2
		if midpoint == target:
			return midpoint
		elif midpoint < target:
				start = midpoint + 1
		else:
			end = midpoint - 1
	return None


# @time_measurement
def recursive_binary_search(list, target):

	if len(list) == 0:
		return False
	
	else:
		midpoint = (len(list)) // 2
		if midpoint == target:
			return midpoint
		else:
			if list[midpoint] < target:
				return recursive_binary_search(list[midpoint+1:], target)
			else:
				return recursive_binary_search(list[:midpoint], target)
	return None






def location(list, index):
	"""It search through the given list to get the location of the target
	   It runs in Linear time - O(n)"""
	position = 0
	while position < len(list):
		for x in list:
			if x != index:
				position += 1
			else:
				return f"Target {x} found at index {position}"
	return f"Target {index} not in list"



linear = linear_search(unsorted_list, 7)
binary = binary_search(sorted_list, 3)
recursive = recursive_binary_search(sorted_list, 9)


print(f"Linear: {location(unsorted_list, linear)}")
print(f"Binary: {location(sorted_list, binary)}")
print(f"Recursive: {location(sorted_list, recursive)}")