def load_maze(filename):
	with open(filename) as f:
		content = f.readlines()
	
	return [v.replace("\n", "") for v in content]


if __name__=="__main__":
	load_maze()