# linked list:
# 1. singly linked list
# 2. doubly linked list

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
		pre = None
		cur = self.head
		nxt = None
		while cur != None:
			nxt = cur.next
			cur.next = pre 
			pre = cur 
			cur = nxt 
		self.head = pre

	def mid_element(self):
		slow = self.head 
		fast = self.head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		return slow.data

		# curr = self.head
		# count = 0 
		# while curr:
		# 	curr = curr.next
		# 	count += 1
		# mid_idx = count//2

		# count = 0
		# curr = self.head
		# while count != mid_idx:
		# 	curr = curr.next 
		# 	count += 1
		# return curr.data

	def dutch(self):
		f0 = None
		l0 = None
		th0 = None

		f1 = None
		l1 = None
		th1 = None

		f2 = None
		l2 = None
		th2 = None

		temp = self.head
		while temp:
			if temp.data == r:
				if f0 == None:
					f0 = temp
					l0 = temp
					th0 = temp
				else:
					f0 = temp
					l0.next = f0
					l0 = f0
			if temp.data == w:
				if f1 == None:
					f1 = temp
					l1 = temp
					th1 = temp
				else:
					f1 = temp
					l1.next = f1
					l1 = f1
			if temp.data == b:
				if f2 == None:
					f2 = temp
					l2 = temp
					th2 = temp
				else:
					f2 = temp
					l2.next = f2
					l2 = f2
			temp = temp.next
		self.head = th0
		l0.next = th1
		l1.next = th2
		l2.next = None
		
	def __str__(self):
		print()
		temp = self.head
		li = []
		while temp:
			li.append('[{0}]-> '.format(temp.data))
			temp = temp.next
		return "".join(li)

	def display(self):
		temp = self.head
		while temp:
			if temp.data == w:
				print(Fore.WHITE + temp.data)
			else:
				print(Fore.RED + temp.data)
			temp = temp.next

li = SingleLinkedList()
w = "white"
r = "red"
b = "blue"
arr = input().split(" ")
for x in arr:
	li.add_at_last(x)

print(li)
li.dutch()
print(li)








# li.add_at_last(10)
# li.add_at_last(20)
# li.add_at_last(30)
# li.add_at_last(40)
# li.add_at_last(50)
# li.add_at_last(60)


# print(li)
# print("count :",li.mid_element())
# # # li.remove_at_index(0) # error
# # li.remove_at_index(0) # error
# # li.reverse()

# # print(li)
# # no elements
# # one elements


