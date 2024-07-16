

class Queue:
	def __init__(self,n):
		self.front = -1
		self.rear = -1
		self.limit = n
		self.arr = [ None for x in range(n) ]

	def incr(self,value):
		return ( value + 1 ) % self.limit

	def enqueue(self,value):
		if self.isFull():
			return

		if self.isEmpty():
			self.front = 0
		# adding elements
		self.rear = self.incr(self.rear)
		self.arr[self.rear] = value

	def dequeue(self):
		if self.isEmpty():				
			return None
		# remove first element
		value = self.arr[self.front]
		self.arr[self.front]=None
		self.front = self.incr(self.front)
		return value

	def __str__(self):
		return "queue : " + str(self.arr)

	def isEmpty(self):
		return self.front == -1 and self.rear == -1
	def isFull(self):
		return self.incr(self.rear) == self.front


q = Queue(4)
q.enqueue(100)
q.enqueue(200)
q.enqueue(300)
q.enqueue(400)
q.enqueue(10) # won't get added
q.enqueue(20) # won't get added

print(q)

print("dequeue : ", q.dequeue())
print("dequeue : ", q.dequeue())

print(q)
q.enqueue(1000)
q.enqueue(2000)
print("dequeue : ",q.dequeue())

print(q)
print("front value : ",q.arr[q.front])
print("rear  value : ",q.arr[q.rear])

# other ways to use queue is
# using collections
 
from collections import deque

# using python list
queue = []
# enqueue
queue.append()
# dequeue
queue.pop(0) # by passing index value 0
# it will remove first element
