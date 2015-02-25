H = 'h'
V = 'v'
horiz = 1
vert = 1
def add_segment(x, y, line):
	global horiz
	global vert
	# Horizontal cut 
	if line[1] == H:
		horiz += 1
		return vert
	else:
		vert += 1
		return horiz

def compute_cost(x, y, horiz_cost, vert_cost):
	horiz_cost = [(val, H, i+1) for i, val in enumerate(horiz_cost)]
	vert_cost = [(val, V, i+1) for i, val in enumerate(vert_cost)]
	cost = horiz_cost + vert_cost
	cost = list(reversed(sorted(cost, key=lambda a: (a[0], a[2]))))
	total_cost = 0
	horiz_counter = 1
	vert_counter = 1
	counter = 1
	M = [[0]*(y) for i in range(x)]
	for c in cost:
		s = add_segment(x, y, c)
		total_cost = total_cost + c[0] * s
		
		
	return total_cost % (10 ** 9 + 7)

if __name__ == "__main__":
	#horiz_cost = [2,1,3,1,4]
	#vert_cost = [4,1,2]
	#x, y = 6, 4
	no_of_case = input()
	
	for i in range(no_of_case):
		x, y = map(int, raw_input().strip().split())
		horiz_cost = map(int, raw_input().strip().split())
		vert_cost = map(int, raw_input().strip().split())
		print compute_cost(x, y, horiz_cost, vert_cost)
		horiz = 1
		vert = 1
	
