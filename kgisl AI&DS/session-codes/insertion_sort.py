
arr = [5,4,3,2,1]
n = len(arr)

def insertionSort(arr,n):
	for i in range(1,n):
		key = arr[i]
		j = i-1
		while j>=0 and arr[j]>key:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key

print(arr)
insertionSort(arr,n)
print(arr)