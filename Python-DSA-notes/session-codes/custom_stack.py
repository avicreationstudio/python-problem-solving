MAX_SIZE = 1000

class Stack:
	def __init__(self,n=-1):
		# initial top value is set to -1
		# For a purpose
		# you will know the reason in push and pop 
		# operations.
		self.top = -1
		if n==-1:
			# if n value is not passed
			# Then it is considered as infinite stack
			self.size = MAX_SIZE
		else:
			# if n is passed
			# limited stack
			self.size = n
		# below code generates n number of None list
		self.arr = [ None ] * n

	def isEmpty(self):
		# as initial value of self.top is set to -1
		if self.top == -1:
			return True
		return False

	def push(self,value):
		if self.isFull():
			return
			# print("stack is full")
		else:
			# push logic
			self.top+=1
			self.arr[self.top] = value

	def pop(self):
		if self.top == -1:
			# print("stack is empty")
			return
		value = self.arr[self.top]
		self.arr[self.top] = None
		self.top-=1
		return value


	def isFull(self):
		# self.top value is nothing but storing
		# index value
		if self.top+1 == self.size:
			return True
		return False

	def peek(self):
		if not self.isEmpty():
			return self.arr[self.top]
		# if stack is empty
		# automatically function will return None

		# print("stack is empty")
		

	def getCount(self):
		# self.top stores index value
		return self.top + 1

	def __str__(self):
		return str("stack: ",str(self.arr))

	def __repr__(self):
		return str("stack: ",str(self.arr))

	def clear(self):
		self.top = -1
		self.arr = [ None ] * self.size

if __name__=="__main__":
	s = Stack()
	s.push('jackie chan')
	s.push('doremon')
	s.push('ninja hatori')
	s.push('choota beem')
	s.push('gloria vin veedu')

	res = s.getCount()

	print(res)


# other ways to create stack is python list

stack = []
# push
stack.append()
# pop
stack.pop()