arr = [1,2,3,4,5,6,7,8,9,10] #list(map(int,input("arr: ").split(" ")))
n = len(arr)

key = int(input("key :"))

# logic 1 : complexity => O(n)
# index = -1
# loop_count = 0
# for i in range(n):
# 	loop_count+=1
# 	if key == arr[i]:
# 		index = i
# 		break

# # logic 2 : complexity => O(log n)
# def binarySearchIteration(arr,n,key):
# 	low = 0
# 	high = n-1
# 	mid = None

# 	while low <= high:
# 		mid = (low + high)//2
# 		if arr[mid] == key:
# 			return mid
# 		else:
# 			if key >= arr[mid]:
# 				low = mid+1
# 			else:
# 				high = mid-1

# 	return -1

# print(binarySearchIteration(arr,n,key))
# # print("found index value : ", mid)
# # print("loop_count",loop_count)


# # logic 3 : complexity => O(log n)
def binary(arr,low,high,key):
	if low > high:
		return -1

	# main logic
	mid = (low + high)//2
	if arr[mid] == key:
		return mid
	else:
		if key >= arr[mid]:
			# low = mid+1
			return binary(arr,mid+1,high,key)
		else:
			# high = mid-1
			return binary(arr,low,high-1,key)

print(binary(arr,0,n-1,key))