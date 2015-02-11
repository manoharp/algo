"""
Newton Raphson method to solve any equations
"""
from functools import partial 

def solve_equations(func, derived_func,close_enough, guess):
	"""
	Generic equation solver using newton Raphson
	func : Function f(x), we are trying to solve f(x) = =
	derived_func: f'(x)
	close_enough: validation

	"""
	f = func(guess)
	df = derived_func(guess)
	cl = close_enough(guess)

	new_guess = guess - f / df
	if cl:
		return new_guess 

	return solve_equations(func, derived_func, close_enough, new_guess)

##############
"""
Implement your own equations. Below are examples for Sqroot and cube
"""
###############
def sqroot(x, n):
	return x**2 - n

def sqroot_deriv(x):
	return 2*x

def close_enough(func, n, guess):
	error = func(guess, n)
	if error < 0.00001:
		return True
	
	return False

def cuberoot(x,n):
	return x**3 - n

def cubroot_deriv(x):
	return 3*x*x

if __name__ == '__main__':
	n = 100
	sq = partial(sqroot, n=n)
	cl = partial(close_enough, sqroot, n)
	print solve_equations(sq, sqroot_deriv, cl, guess=float(n/2))

	cb = partial(cuberoot, n=n)
	cl1 = partial(close_enough, cuberoot, n)
	print solve_equations(cb, cubroot_deriv, cl1, guess=float(n/3))
	
