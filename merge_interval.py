from collections import namedtuple
Point = namedtuple('Point', ['start', 'end'])

class Stack(list):
	def peek(self):
		return list.__getitem__(self, -1)

a = [(1,3), (5,9), (2,4), (7,10), (6,80)]
a = sorted(a, key=lambda x:x[0])
print a

results = []
s = Stack()
# Initalize the stack with the first element
s.append(Point(*a[0]))

for i in range(1, len(a)):
	curr = Point(*a[i])
	prev = s.peek()
	
	if prev.end >= curr.start:
		# Has Overlap
		print "P: {0} C: {1}".format(prev,curr)
		new_start = prev.start if prev.start < curr.start else curr.start
		new_end = prev.end if prev.end > curr.end else curr.end
		s.pop()
		s.append(Point(new_start, new_end))
	else:
		s.append(curr)


for i in s:
	print i
