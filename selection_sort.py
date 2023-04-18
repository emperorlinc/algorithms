from time_measurement import time_measurement

@time_measurement
def selection_sort(values):

	sorted_list = []
	print("%-25s %-25s" % (values, sorted_list))
	for i in range(0, len(values)):
		index_to_move = index_of_min(values)
		sorted_list.append(values.pop(index_to_move))
		print("%-25s %-25s" % (values, sorted_list))
	return sorted_list


def index_of_min(values):
	min_index = 0
	for i in range(1, len(values)):
		if values[i] < values[min_index]:
			min_index = i
	return min_index


my_list = [3, 5, 2, 0, 1, 4, 7, 6, 9, 8]

print(selection_sort(my_list))