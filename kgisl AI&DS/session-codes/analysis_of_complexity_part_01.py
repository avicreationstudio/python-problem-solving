# sudo code:

# for(i = 1; i <=n ; i = i + 1 )
#   print 'hello'
for i in range(1,n+1):
	print('hello')
# time complexity
# O(n)

# ------------------------------------

# for(i = 1; i <=n ; i = i + 2 )
#   print 'hello'
for i in range(1,n+1,2):
	print('hello')
# time complexity
# O(n/2) -> O(n/2)

# ------------------------------------

# for(i = n/2; i >=1 ; i = i - 1 )
#   print 'hello'
for i in range(n/2,1-1,-1):
	print('hello')
# time complexity
# O(n/2) -> O(n/2)

# ------------------------------------

# for(i = 1; i < n ; i = i * 2 )
#   print 'hello'
i = 1
while i < n:
	print("hello")
	i = i * 2
# time complexity
# O(log n)

# ------------------------------------

i = s = 1
while s <= n:
	print("hello")
	i = i + 1
	s = s + i

# k(k+1)    
# ------		= 	n      
#   2

# k^2 + k
# -------		=	n
#   2

# k^2			=  	n 

# k = sqrt(n)

# # complexity
# O(sqrt(n))
# ------------------------------------

for i in range(sqrt(n)):
	pass

# # complexity
# O(sqrt(n))
# ------------------------------------

i = n 
while i>1:
	i = i/2

# # complexity
# O(log n)
# ------------------------------------

i = j = 1
while i < n:
	i = 2**2**j
	j = j + 1 

# # complexity
# O(log log n)
# ------------------------------------
for i in range(n):
	for j in range(n):
		pass

# # complexity
# O(n^2)
# ------------------------------------
for i in range(n):
	for j in range(n):
		for k in range(n):
			pass

# # complexity
# O(n^3)
# ------------------------------------

