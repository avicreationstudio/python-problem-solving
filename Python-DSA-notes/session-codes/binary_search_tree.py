from collections import deque

class Node:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

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


def insert(node,key):
	if node == None:
		return Node(key)
	if node.data == key:
		return node
	elif key < node.data:
		node.left = insert(node.left,key)
	else:
		node.right = insert(node.right,key)
	return node

def search(node,key):
	if node == None:
		return False
	if node.data == key:
		return True
	elif key < node.data:
		return search(node.left,key)
	else:
		return search(node.right,key)

def delete(node,key):
	if node.data == key:
		return None
	elif key < node.data:
		node.left = delete(node.left,key)
	else:
		node.right = delete(node.right,key)
	return node

root = None
root = insert(root,10)
root = insert(root,5)
root = insert(root,15)
root = insert(root,7)
root = insert(root,11)
root = insert(root,17)
root = insert(root,8)
root = insert(root,10)


delete(root,8)
level_order_level(root)

# print("search : ",search(root,100))
