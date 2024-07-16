class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10 # again connected
n10.next = n3

head = n1 
slow = head
fast = head
slow = slow.next
fast = fast.next.next

while slow != fast:
	slow = slow.next 
	fast = fast.next.next
	if fast.next == None:
		break

print("condition 01 :", fast.data)
print("condition 02 : ", slow == fast)

if slow == fast:
	print("loop detected")
else:
	print("no loop detected")