class Heap:
	def __init__(self):
		self.arr = []
		self.size = 0
		# self.limit = 5

	def get_parent(self,child_idx):
		return (child_idx - 1)//2

	def get_left_child(self,parent_idx):
		return (2*parent_idx) + 1

	def get_right_child(self,parent_idx):
		return (2*parent_idx) + 2
	
	def heapify_BU(self,i):
		parent_idx = self.get_parent(i)

		if parent_idx >= 0 and self.arr[i] > self.arr[parent_idx]:
			self.arr[i],self.arr[parent_idx] = self.arr[parent_idx],self.arr[i]
			self.heapify_BU(parent_idx)

	def insert(self,data):
		self.arr.append(data)
		self.size += 1
		# if self.size == 1:
		# 	return
		self.heapify_BU(self.size - 1)

	def heapify_TB(self,i):
		l = self.get_left_child(i)
		r = self.get_right_child(i)
		largest_idx = i 
		if l < self.size and self.arr[l] > self.arr[largest_idx]:
			largest_idx = l 
		if r < self.size and self.arr[r] > self.arr[largest_idx]:
			largest_idx = r 
		if largest_idx != i:
			self.arr[largest_idx],self.arr[i] = self.arr[i],self.arr[largest_idx]
			self.heapify_TB(largest_idx)

	def delete(self):
		if self.size == 0:
			return None
		if self.size == 1:
			self.size -= 1 
			return self.arr.pop()

		root = self.arr[0] # root value
		last_ele = self.arr.pop()
		self.arr[0] = last_ele
		self.size -= 1
		self.heapify_TB(0)

		return root


	def __str__(self):
		return " ".join(list(map(str,self.arr)))

heap = Heap()
heap.insert(10)
heap.insert(20)
heap.insert(2)
heap.insert(50)
heap.insert(3)

print(heap)
print("deleted : ",heap.delete())
print(heap)