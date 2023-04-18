import sys
from load_maze import load_maze

maze = load_maze(sys.argv[1])

def solve_maze(maze):
	solved_maze = []
	for i in maze:
		for v in i:
			if v == " ":
				v = "*"
			solved_maze.append(v)

	return solved_maze


def format_maze(values):
	index, const, v = 19, 19, 2
	for i in range(1, len(values)):
		if i == index:
			values.insert(index, "\n")
			index = const * v
			v += 1
			index += 1

	return "".join(values)
	


print(format_maze(solve_maze(maze)))
