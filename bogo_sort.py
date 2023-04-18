import random
from time_measurement import time_measurement


def is_sorted(list):
	for index in range(len(list) - 1):
		if list[index] > list[index + 1]:
			return False
	return True

@time_measurement
def bogo_sort(values):
	while not is_sorted(values):
		random.shuffle(values) 
	return values

my_list = [3, 0, 8, 7, 1, 4, 2]


sorted_list = bogo_sort(my_list)


print(sorted_list)
