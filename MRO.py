"""
MRO : Method Resolution Order
Use C3 Linearization.

The merge of parents' linearizations and parents list is done by selecting the first head of the lists, which does not appear in the tail of any of the lists.

Output:
Calling Child1
In SubB
In SubA # Notice Super SubB calls SubA not A first
In Base A
In SubA after calling Super...
In SubB after calling Super....
==========
Calling Child2
In SubB
In Base A
In SubB after calling Super....
"""

class BaseA(object):
	def __init__(self):
		print "In Base A"

class BaseB(object):
	def __init__(self):
		print "In Base B"

class BaseC(object):
	def __init__(self):
		print "In Base C"


class SubA(BaseA):
	def __init__(self):
		print "In SubA"
		super(SubA, self).__init__()
		print "In SubA after calling Super..."

class SubB(BaseA, BaseB, BaseC):
	def __init__(self):
		print "In SubB"
		super(SubB, self).__init__()
		print "In SubB after calling Super...."

class Child1(SubB, SubA):
	def __init__(self):
		print "Calling Child1"
		super(Child1, self).__init__()

class Child2(SubB):
	def __init__(self):
		print "Calling Child2"
		super(Child2, self).__init__()

def main():
	x = Child1()
	print "=" * 10
	x = Child2()

if __name__ == '__main__':
	main()

