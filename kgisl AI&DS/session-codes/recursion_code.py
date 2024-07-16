# # # # Recursion:
# # # # 	function that calls itself directly
# # # # 	or indirectly is called Recursion

# # # # directly:
# # # # 	- head
# # # # 	- tail
# # # # 	- tree
# # # # 	- nested
# # # # 	- linear

# # # # indirectly:
# # # # - head recursion


# # # # def fn1(n):
# # # # 	if n>=1:
# # # # 		# head recursion
# # # # 		fn1(n-1)
# # # # 		print("logic",n)

# # # # def fn2(n):
# # # # 	if n>=1:
# # # # 		# tail recursion
# # # # 		print("logic",n)
# # # # 		fn2(n-1)

# # # # fn1(3)
# # # # print("---------")
# # # # fn2(3)

# # # n = 3
# # # for i in range(1,n+1):
# # # 	print("logic", i)

# # # print("----------")
# # # n = 3
# # # for i in range(1,n+1):
# # # 	print("logic", n-i+1)

# # # linear recursion

# # n= 5
# # def fn(x) -> None:
# # 	if n==x:
# # 		print("func executed")
# # 		fn(x-1)

# # n = 10
# # fn(10)



# # # - tree recursion
# # count = 0

# # def fn(n):
# # 	global count
# # 	# print("executed",n)
# # 	count=count+1
# # 	if n>0:
# # 		fn(n-1)
# # 		fn(n-1)

# # fn(5)
# # print(count)

# # # 2 - 7
# # # 3 - 15
# # # 4 - 31
# # # 5 - 63



# # nested recursion

# def fn(n):
# 	print("func",n)
# 	if n == 1:
# 		return 1

# 	return fn(fn(n-1))


# fn(3)

# indirect recursion

# def fn1():
# 	print("hai 1")
# 	fn2()

# def fn2():
# 	print("hello 2")


# fn1()



