# linked list:
# 1. singly linked list

# singly linked list

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

class SingleLinkedList:
	def __init__(self):
		self.head = None

	def add_at_front(self,data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def add_at_last(self,data):
		new_node = Node(data)
		if self.head == None:
			self.head = new_node
		else:
			temp = self.head
			while temp.next:
				temp = temp.next
			temp.next = new_node
		
	def add_at_index(self,data,index):
		if index <= 0:
			self.add_at_front(data)
			return

		new_node = Node(data)
		temp = self.head
		idx = 0
		while temp != None and idx != index - 1:
			temp = temp.next
			idx += 1
		if temp == None:
			# reached end of element
			self.add_at_last(data)
			return
		new_node.next = temp.next
		temp.next = new_node

	def isExists(self,key):
		temp = self.head
		while temp != None:
			if key == temp.data:
				return True
			temp = temp.next

		return False

	def remove_at_front(self):
		if self.head == None:
			return

		temp = self.head
		self.head = self.head.next
		temp.next = None

	def remove_at_last(self):
		if self.head == None:
			return
		if self.head.next == None:
			self.head = None
			return

		curr = self.head
		while curr.next.next:
			curr = curr.next
				
		curr.next = None


	def remove_at_index(self,position):
		if position < 0:
			return
		if position == 0:
			self.remove_at_front()
			return
		curr = self.head
		index = 0
		while curr and index != position - 1:
			curr = curr.next 
			index += 1
		if curr == None:
			return
		temp = curr.next
		curr.next = temp.next
		temp.next = None

	def reverse(self):
		# TODO: 01
		pass

	def mid_element(self):
		# TODO: 02
		pass

	def poland(self):
		# TODO: 03
		pass
		
	def __str__(self):
		print()
		temp = self.head
		li = []
		while temp:
			li.append('[{0}]-> '.format(temp.data))
			temp = temp.next
		return "".join(li)

li = SingleLinkedList()


