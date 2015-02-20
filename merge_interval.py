from collections import namedtuple
Point = namedtuple('Point', ['start', 'end', 'contains'])

class Stack(list):
	def peek(self):
		return list.__getitem__(self, -1)

a = [(1,4), (5,9), (2,4), (7,10), (6,80)]
a = sorted(a, key=lambda x:x[0])

results = []
s = Stack()

# Initalize the stack with the first element
_start = Point(*a[0],contains=[])
_start = _start._replace(contains=[_start])
s.append(_start)

for i in range(1, len(a)):
	curr = Point(*a[i], contains=[])
	prev = s.peek()
	
	if prev.end >= curr.start:
		# Has Overlap
		new_start = prev.start if prev.start < curr.start else curr.start
		new_end = prev.end if prev.end > curr.end else curr.end

		contains = prev.contains
		contains.append(curr)

		s.pop()
		s.append(Point(new_start, new_end, contains))
	else:
		curr = curr._replace(contains=[curr])
		s.append(curr)


for i in s:
	print "***"
	print i.start , i.end
	child = i.contains
	for c in child: print c
