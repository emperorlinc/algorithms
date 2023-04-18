import numbers

def merge_sort(list):
	if len(list) <= 1:
		return list

	left_half, right_half = split(list)
	left = merge_sort(left_half)
	right = merge_sort(right_half)

	return merge(left, right)


def split(list):

	mid = len(list) // 2
	left = list[:mid]
	right = list[mid:]

	return left, right


def merge(left, right):
	l = []
	x = 0
	y = 0

	while x < len(left) and y < len(right):
		if left[x] < right[y]:
			l.append(left[x])
			x += 1
		else:
			l.append(right[y])
			y += 1

	while x < len(left):
		l.append(left[x])
		x += 1

	while y < len(right):
		l.append(right[y])
		y += 1

	return l

names = [
	"Balogun Basit",
	"Olowoyo James",
	"Adeyemi Kehinde",
	"Ejalonibu Dolapo",
	"Hassan Abdul-Roheem",
	"Adeosun Opeyemi",
	"Ibrahim-Oke Mas'ud",
	"Ibironke Omololade",
	"John Doe",
	"Olayori Ololade",
	"Oloyede Peter"
]



result = merge_sort([5,3,9,0,7,1,6,2,8,4])

print(result)
