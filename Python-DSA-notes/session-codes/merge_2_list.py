# write a program to merge 2 linked list
# where you are provided with heads of 2 linked list

class Node:
	def __init__(self,data):
		self.data = data
		self.next = None

def display(head):
	curr = head 
	while curr:
		print(curr.data,end=" ")
		curr = curr.next
	print() 

def mergeList(head1,head2) -> Node :
	# conditions:
	# 	 list with less count should come first
	#    list with more count should come next
	#    return merged list head
	curr1 = head1
	curr2 = head2
	while curr1 and curr2:
		if curr1.next == None:
			curr1.next = head2
			return head1
			
		elif curr2.next == None:
			curr2.next = head1
			return head2

		curr1 = curr1.next
		curr2 = curr2.next
		
	if curr1:
		return head1
	elif curr2:
		return head2
	else:
		return None



head1 = Node(10)
head1.next = Node(20)
head1.next.next = Node(30)
head1.next.next.next = Node(40)

head2 = Node(11)
head2.next = Node(22)

# head1 = None
# head2 = None

display(head1)
display(head2)
new_head = mergeList(head1,head2)
# print(new_head)
display(new_head)

