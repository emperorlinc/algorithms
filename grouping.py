def grouping(list):
	nested_list = []
	while len(list) > 0:
		value = list.pop(0)
		value2= list.pop(0)
		nested_list.append([value, value2])
	return nested_list

my_list = [1,2,3,4,5,6,7,8,9,0]

result = grouping(my_list)
print(result)