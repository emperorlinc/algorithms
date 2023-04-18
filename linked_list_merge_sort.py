from linked_list import LinkedList

def merge_sort(linked_list):

	if linked_list.len() <= 1:
		return linked_list

	left_half, right_half = split(linked_list)

	left = merge_sort(left_half)
	right = merge_sort(right_half)

	return merge(left, right)


def split(linked_list):

	# DC