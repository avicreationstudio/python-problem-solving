
# quick sort: sorting algorithm

arr = [1.0,1.01,2.0,0.001,0.01]
n = len(arr)

def partition(arr,low,high):
	pivot = arr[high]
	pi = low
	for j in range(low,high):
		if arr[j] <= pivot:
			# swap
			arr[j],arr[pi] = arr[pi],arr[j]
			pi += 1
	arr[pi],arr[high] = arr[high],arr[pi]

	return pi

def quickSort(arr,low,high):
	if low < high:
		pi = partition(arr,low,high)
		quickSort(arr,low,pi-1)
		quickSort(arr,pi+1,high)


quickSort(arr,0,n-1);
print(arr)