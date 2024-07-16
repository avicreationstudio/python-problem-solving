
arr = [1,2,3,4,5]
n = len(arr)

def bubblesort():
	for i in range(n-1):
		is_swap_happened = False
		print("iteration",i)
		for j in range(n-i-1):
			print("steps",j)
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
				is_swap_happened = True

			print()
		if not is_swap_happened:
			break
		
bubblesort()
print(arr)

# points
# 1. swapping is the main logic
# 2. main logic is written inside for loop using j index value
# 3. we are using n-1 because, we don't want to compare last element
# 4. running for loop j index, for only once is not enough
# 5. Hence using another for loop called "for loop i"
# 6. we are using n-i because, in each iteration sorted 
#    value will be available at end

# 7. adding n-1 in line 6, bcz running loop for n times is unneccessary
#    as n-1 times itself solving the worst case scenario [5,4,3,2,1]


