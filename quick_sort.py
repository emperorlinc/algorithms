# import sys
# import load_names


# names = load_names(sys.argv[1])

def quick_sort(values):
	if len(values) <= 1:
		return values

	less_than_pivot = []
	greater_than_pivot = []
	pivot = values[0]

	for value in values[1:]:
		if value <= pivot:
			less_than_pivot.append(value)
		else:
			greater_than_pivot.append(value)
	print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
	return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)






result = quick_sort(load_numbers)

print(result)











# names = [
# 	"Balogun Basit",
# 	"Olowoyo James",
# 	"Adeyemi Kehinde",
# 	"Ejalonibu Dolapo",
# 	"Hassan Abdul-Roheem",
# 	"Adeosun Opeyemi",
# 	"Ibrahim-Oke Mas'ud",
# 	"Ibironke Omololade",
# 	"John Doe",
# 	"Olayori Ololade",
# 	"Oloyede Peter"
# ]
# result = quick_sort(names)
# print(result)



# unsorted_list = [3,2,6,7,1,9,4,0,8,5]
# result = quick_sort(unsorted_list)
# print(result)
