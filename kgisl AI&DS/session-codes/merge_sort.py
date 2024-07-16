
def merger(arr,start,mid,end):
	ls = mid - start + 1
	rs = end - mid

	la = arr[start:start+ls]
	ra = arr[mid+1:mid+ls+1]
	
	# for i in range(ls):
	# 	la[i] = arr[i+start]
	# for i in range(rs):
	# 	ra[i] = arr[i+mid+1]

	i = j = 0
	k = start
	while i < ls and j < rs :
		if la[i] < ra[j]:
			arr[k] = la[i]
			i+=1
		else:
			arr[k] = ra[j]
			j+=1
		k+=1

	while i < ls:
		arr[k] = la[i]
		i += 1
		k += 1

	while j < rs:
		arr[k] = ra[j]
		j += 1
		k += 1
	# end of merger

def mergeSort(arr,start,end):
	if start < end:
		mid = ( start + end )//2
		mergeSort(arr,start,mid)
		mergeSort(arr,mid+1,end)
		merger(arr,start,mid,end)

arr = [5,4,3,2,1,0]
n = len(arr)
mergeSort(arr,0,n-1)
print(arr)
