def load_numbers(filename):
	with open(filename) as f:
		content = f.readlines()

	return [int(val.replace("\n", "")) for val in content]


if __name__=="__main__":
	load_numbers()