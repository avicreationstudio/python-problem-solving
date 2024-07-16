from collections import deque

class Node:
	def __init__(self,data):
		self.data = data 
		self.left = None
		self.right = None

	def __str__(self):
		return str(self.data)

def inorder(node):
	if node != None:
		inorder(node.left)		  # left
		print(node.data,end=" ")  # root
		inorder(node.right)		  # right

def inorder_iterative(root):
	curr = root
	s = []
	while True:
		while curr:
			s.append(curr)
			curr = curr.left 

		# loop break
		if len(s) == 0:
			break

		# print node data
		curr = s.pop()
		print(curr.data,end=" ")

		# travel right side
		curr = curr.right



def preorder(node):
	if node != None:
		print(node.data,end=" ")  	# root
		preorder(node.left)  		# left
		preorder(node.right)		# right

def preorder_iterative(node):
	# root left right
	curr = root
	s = []
	while True:
		while curr:
			print(curr.data,end=" ")  # changes
			s.append(curr)
			curr = curr.left 

		# loop break
		if len(s) == 0:
			break

		# print node data
		curr = s.pop()

		# travel right side
		curr = curr.right


def postorder(node):
	if node != None:
		postorder(node.left)		# left
		postorder(node.right)		# right
		print(node.data,end=" ")	# root

def postorder_iterative(root):
	ans = []
	travel = []
	curr = root
	travel.append(curr)
	while len(travel) != 0:
		curr = travel.pop()
		ans.append(curr.z)
		if curr.left:
			travel.append(curr.left) 
		if curr.right:
			travel.append(curr.right)

	while len(ans) != 0:
		print(ans.pop(),end=" ")


def level_order(node):
	q = deque()
	curr = node
	q.appendleft(curr) # enqueue
	while len(q) != 0:
		curr = q.pop() # dequeue
		print(curr.data,end=" ")
		if curr.left:
			q.appendleft(curr.left) # enqueue
		if curr.right:
			q.appendleft(curr.right) # enqueue


def level_order_level(node):
	q = deque()
	curr = node
	q.appendleft(curr) # enqueue
	while len(q) != 0:
		size = len(q)
		while size > 0:
			curr = q.pop() # dequeue
			print(curr.data,end=" ")
			size -= 1
			if curr.left:
				q.appendleft(curr.left) # enqueue
			if curr.right:
				q.appendleft(curr.right) # enqueue
		print()


def zig_zag_order(node):
	q = deque()
	curr = node
	q.appendleft(curr) # enqueue
	rev = -1
	while len(q) != 0:
		size = len(q)
		li = []
		while size > 0:
			curr = q.pop() # dequeue
			li.append(curr.data)
			size -= 1
			if curr.left:
				q.appendleft(curr.left) # enqueue
			if curr.right:
				q.appendleft(curr.right) # enqueue
		print(li[::rev])
		rev = -rev

def left_view(node):
	q = deque()
	curr = node
	q.appendleft(curr) # enqueue
	while len(q) != 0:
		size = len(q)
		li = []
		while size > 0:
			curr = q.pop() # dequeue
			li.append(curr.data)
			size -= 1
			if curr.left:
				q.appendleft(curr.left) # enqueue
			if curr.right:
				q.appendleft(curr.right) # enqueue
		print(li[0])

def right_view(node):
	q = deque()
	curr = node
	q.appendleft(curr) # enqueue
	while len(q) != 0:
		size = len(q)
		li = []
		while size > 0:
			curr = q.pop() # dequeue
			li.append(curr.data)
			size -= 1
			if curr.left:
				q.appendleft(curr.left) # enqueue
			if curr.right:
				q.appendleft(curr.right) # enqueue
		print(li[-1])


def boundary(node):
	q = deque()
	curr = node
	q.appendleft(curr) # enqueue
	levels = []
	while len(q) != 0:
		size = len(q)
		li = []
		while size > 0:
			curr = q.pop() # dequeue
			li.append(curr.data)
			size -= 1
			if curr.left:
				q.appendleft(curr.left) # enqueue
			if curr.right:
				q.appendleft(curr.right) # enqueue
		levels.append(li)
	# left view
	for lvl in levels:
		print(lvl[0],end=" ")
	# bottom view
	print(*levels[-1][1:-1],end=" ")
	# right view
	for lvl in levels[::-1]:
		print(lvl[-1],end=" ")

def count(node):
	if node == None:
		return 0
	ls = count(node.left)
	rs = count(node.right)
	return 1 + ls + rs


def count_leaf(node):
	if node == None:
		return 0
	if node.left == None and node.right == None:
		return 1
	ls = count_leaf(node.left)
	rs = count_leaf(node.right)
	return ls + rs

def leaf_nodes(node):
	if node == None:
		return
	if node.left == None and node.right == None:
		print(node.data, end=" ")
	leaf_nodes(node.left)
	leaf_nodes(node.right)
	

def count_non_leaf(node):
	if node == None:
		return 0
	if node.left == None and node.right == None:
		return 0
	ls = count_non_leaf(node.left)
	rs = count_non_leaf(node.right)
	return 1 + ls + rs


def height(node):
	if node == None:
		return 0
	ls = height(node.left)
	rs = height(node.right)
	return 1 + max([ls,rs])

def isBalance(root):
	lst = height(root.left)
	rst = height(root.right)
	res = abs( lst - rst )
	if res > 1:
		return False
	return True


def sum_of_nodes(node):
	if node == None:
		return 0
	lsum = sum_of_nodes(node.left)
	rsum = sum_of_nodes(node.right)	
	return node.data + lsum + rsum


def sum_of_leaf_nodes(node):
	if node == None:
		return 0
	if node.left == None and node.right == None:
		return node.data	
	lsum = sum_of_leaf_nodes(node.left)
	rsum = sum_of_leaf_nodes(node.right)	
	return lsum + rsum

def mirror(node):
	if node == None:
		return
	mirror(node.left)
	mirror(node.right)
	# swap
	node.left ,node.right = node.right, node.left


s = set([5])
s.add(1)
s.add(10)
s 

# 1 5 10 # sorted
# 5 1 10 # order preserved




# # creating tree
# level 0
root = Node(10)
# level 1 
root.left = Node(20)
root.right = Node(30)
# level 2
root.left.left = Node(40)
root.left.right = Node(50)
# level 3
root.left.right.left = Node(80)
root.left.left.left = Node(90)
mirror(root)
level_order_level(root)






# print("\ninorder : recursion ")
# inorder(root)
# print("\ninorder : iterative ")
# inorder_iterative(root)
# print("\npost order: recursion")
# postorder(root)
# print("\npost order: iterative")
# postorder_iterative(root)
# print('\npostorder:')
# postorder(root)













