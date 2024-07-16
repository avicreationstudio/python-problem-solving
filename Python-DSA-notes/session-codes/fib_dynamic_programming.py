

def fib(n):
	global dynamic_array
	if n<=1:
		return n 
	if dynamic_array[n] == None:
		res = fib(n-2) + fib(n-1)
		dynamic_array[n] = res
	return dynamic_array[n]


dynamic_array = [None] * (n + 1)
dynamic_array[0] = 0
dynamic_array[1] = 1

fib(n)