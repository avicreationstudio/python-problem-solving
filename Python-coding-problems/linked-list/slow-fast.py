class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    # find mid element in linked list
    def midElement(self,head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        print(slow.data)

    def reverse(self,head):
        prev = None
        curr = head
        nxt = None
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head = prev
        return head

    def isCircular(self,head):
        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        else:
            return False
    def traverse(self,head):
        temp = head
        while temp != None:
            print(temp.data,end="->")
            temp = temp.next
        else:
            print("None")

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)
n6 = Node(60)
n7 = Node(70)
n8 = Node(80)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n4

head = n1
sol = Solution()
# sol.traverse(head)
# sol.midElement(head)
# head = sol.reverse(head)
res = sol.isCircular(head)
print(res)
# sol.traverse(head)