class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None 

n10 = Node(10)
n20 = Node(20)
n30 = Node(30)
n40 = Node(40)
n50 = Node(50)
n60 = Node(60)
n70 = Node(70)
n80 = Node(80)

n10.left = n20
n10.right = n30

n20.left = n40

n30.left = n50
n30.right = n60

n40.left = n70
n40.right = n80 

root = n10 


def inOrder(node):
    # base case
    if node == None:
        return 
    inOrder(node.left)
    print(node.data,end=" ")
    inOrder(node.right)

def inOrder_iter(root):
    stack = []
    curr = root 
    while True:
        # while to travel left side
        while curr != None:
            stack.append(curr)
            curr = curr.left 
        # to stop the loop
        if len(stack) == 0:
            break
        # root node
        curr = stack.pop()
        print(curr.data, end=" ")
        # travel right side
        curr = curr.right



def preOrder(node):
    # base case
    if node == None:
        return 
    print(node.data,end=" ")
    preOrder(node.left)
    preOrder(node.right)


def preOrder_iter(root):
    stack = []
    curr = root 
    while True:
        # while to travel left side
        while curr != None:
            print(curr.data, end=" ") # 😲 changes
            stack.append(curr)
            curr = curr.left 
        # to stop the loop
        if len(stack) == 0:
            break
        # root node
        curr = stack.pop()
        # travel right side
        curr = curr.right

def postOrder(node):
    # base case
    if node == None:
        return 
    postOrder(node.left)
    postOrder(node.right)
    print(node.data,end=" ")

def iter_postOrder(root):
    # initialization
    travel_stack = []
    answer_stack = []
    curr = root
    travel_stack.append(curr) 
    while len(travel_stack) != 0:
        curr = travel_stack.pop()
        answer_stack.append(curr.data)

        if curr.left:
            travel_stack.append(curr.left)
        if curr.right:
            travel_stack.append(curr.right)

    print(*answer_stack[::-1])

from collections import deque
def levelOrder(root):
    q = deque()
    curr = root 
    q.appendleft(curr) 
    while len(q) != 0:
        size = len(q)
        while size > 0:
            curr = q.pop()
            print(curr.data,end=" ")
            size -= 1 
            if curr.left:
                q.appendleft(curr.left)
            if curr.right:
                q.appendleft(curr.right)
        print() # we have to add this to print levels in new line
        # which is nothing but level by level order.


def leftView(root):
    q = deque()
    curr = root 
    q.appendleft(curr) 
    while len(q) != 0:
        size = len(q)
        li = []
        while size > 0:
            curr = q.pop()
            li.append(curr.data)
            size -= 1 
            if curr.left:
                q.appendleft(curr.left)
            if curr.right:
                q.appendleft(curr.right)
        print(li[0],end=" ")
    
def rightView(root):
    q = deque()
    curr = root 
    q.appendleft(curr) 
    while len(q) != 0:
        size = len(q)
        li = []
        while size > 0:
            curr = q.pop()
            li.append(curr.data)
            size -= 1 
            if curr.left:
                q.appendleft(curr.left)
            if curr.right:
                q.appendleft(curr.right)
        print(li[-1],end=" ")

def zigZag(root):
    q = deque()
    curr = root 
    q.appendleft(curr) 
    flag = -1
    while len(q) != 0:
        size = len(q)
        li = []
        while size > 0:
            curr = q.pop()
            li.append(curr.data)
            size -= 1 
            if curr.left:
                q.appendleft(curr.left)
            if curr.right:
                q.appendleft(curr.right)
        flag = 1 if flag == -1 else -1 
        print(*li[::flag])



 
# inOrder(root); print(" <- inOrder") 
# inOrder_iter(root); 
# preOrder(root); print(" <- preOrder")
# preOrder_iter(root) 
# postOrder(root); print(" <- postOrder")
# iter_postOrder(root);
zigZag(root)