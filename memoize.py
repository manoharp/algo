class memoize(object):
 """
 Memoize wrapper for python
 
 usage:
 @memoize
 def fib(n):
    pass
    
 """
	def __init__(self, function):
		self.function = function
		self.memoized = {}

	def __call__(self, *args):
		try:
			return self.memoized[args]
		except KeyError:
			self.memoized[args] = self.function(*args)
			return self.memoized[args]
