class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def traverse(self, head):
        # traverse
        temp = head
        while temp != None:
            print(temp.data, end='->')
            temp = temp.next
        else:
            print("None")

    def addAtFront(self, head, data):
        new_node = Node(data)
        if head == None:
            head = new_node
            return head
        new_node.next = head
        head = new_node
        return head
    def addAtLast(self,head,data):
        new_node = Node(data)
        if head == None:
            head = new_node
            return head
        temp = head
        while temp.next != None:
            temp = temp.next
        temp.next = new_node
        return head

    def addAtIndex(self, head, data, index):
        if index <= 0:
            head = self.addAtFront(head,data)
            return head
        temp = head
        count = 0
        while temp != None and count != index - 1:
            temp = temp.next
            count += 1
        if temp == None:
            head = self.addAtLast(head,data)
            return head
        new_node = Node(data)
        new_node.next = temp.next
        temp.next = new_node
        return head
    def isExists(self,head,key):
        temp = head
        while temp != None:
            if temp.data == key:
                return True
            temp = temp.next
        return False
    def removeAtFront(self, head):
        if head == None:
            return head
        temp = head
        head = head.next
        temp.next = None
        return head
    def removeAtLast(self,head):
        if head == None:
            return
        if head.next == None:
            head = None
            return
        temp = head
        while temp.next.next != None:
            temp = temp.next
        temp.next = None

    def removeAtIndex(self,head, index):
         if index < 0:
             return head
         if index == 0:
            head = self.removeAtFront(head)
            return head
         temp = head
         count = 0
         while temp != None and count != index - 1:
             temp = temp.next
             count += 1
         if temp == None:
             return head
         delNode = temp.next
         temp.next = delNode.next
         delNode.next = None
         return head

head = None
sol = Solution()
head = sol.addAtIndex(head,10,-2) # it will do addAtFront
head = sol.addAtLast(head,20)
head = sol.addAtLast(head,30)
head = sol.addAtLast(head,40)
head = sol.addAtIndex(head, 50, 100) # it will do addAtLast
sol.traverse(head)
head = sol.addAtIndex(head, 100, 3)
sol.traverse(head)
# print("validating removeAtIndex")
# head = sol.removeAtIndex(head, -10)
# sol.traverse(head)
# head = sol.removeAtIndex(head, 0)
# sol.traverse(head)
# head = sol.removeAtIndex(head, 2)
# sol.traverse(head)
# head = sol.removeAtIndex(head, 11)
# sol.traverse(head)