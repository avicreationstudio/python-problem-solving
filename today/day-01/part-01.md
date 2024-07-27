# linked list

## Base code

```python
class Node:
    def __init__(self, data, next = None):
       self.data = data 
       self.next = next

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
       count_idx = 0
       while temp != None and count_idx != index - 1:
         temp = temp.next
         count_idx += 1
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

       temp = self.head
       while temp.next.next:
         temp = temp.next
          
       temp.next = None


    def remove_at_index(self,position):
       if position < 0:
         return
       if position == 0:
         self.remove_at_front()
         return
       temp = self.head
       index = 0
       while temp and index != position - 1:
         temp = temp.next 
         index += 1
       if temp == None:
         return
       toDelete = temp.next
       temp = temp.next.next
       toDelete.next = None

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        else:
            print("None")

```
