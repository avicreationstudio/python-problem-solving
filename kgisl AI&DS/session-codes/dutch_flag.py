def dutch_flag(arr,n):
	low = 0
	high = n - 1
	i = 0 # can also be taken as mid
	while i <= high:
		if arr[i] == 0:
			arr[i],arr[low] = arr[low],arr[i]
			low += 1
			i+=1
		elif arr[i] == 1:
			i += 1
		else:
			arr[i],arr[high] = arr[high],arr[i]
			high -= 1 
	print(arr)

# dutch flag
# 0 1 2 reprsents 3 colors
arr = [0,0,2,1,0,2,1,0,1,2,1,2] 
n = len(arr)

dutch_flag(arr,n)
print(arr)

