# Problem: Next Greater Element II

    Next Greater Element (NGE) for every element in given Array

**Problem Description:**

The Next greater Element for an element x is the first greater element on the right side of x in the array. Elements for which no greater element exist, consider the next greater element as -1.

For example:

    Input: arr[] = [ 4 , 5 , 2 , 25 ]
    Output:        4      –>   5
                   5      –>   25
                   2      –>   25
                   25     –>   -1
    Explanation: except 25 every element has an element greater than them present on the right side
    
    Input: arr[] = [ 13 , 7, 6 , 12 ]
    Output:         13      –>    -1
                    7       –>     12
                    6       –>     12
                    12      –>     -1
    Explanation: 13 and 12 don’t have any element greater than them present on the right side

### Solution

1. Initialization:

    `stack`: Used to keep track of elements for which we need to find the next greater element.
    `nge_dict`: A dictionary to store the next greater element for each element in the array.

1. Main Logic:

- Iterate through each element in the array:
  - While the stack is not empty and the top element of the stack is less than the current element:
    - Pop the element from the stack and set its next greater element in `nge_dict` to the current element.
  - Push the current element onto the stack.

1. Post-processing:
    - After iterating through the array, for any remaining elements in the stack, set their next greater element to `-1` in `nge_dict`.
1. Printing Results:
    - Iterate through the original array and print the next greater element for each element using `nge_dict`.

#### Time and Space Complexity

- **Time Complexity**: \(O(n)\), where \(n\) is the size of the array `nums`. We make a single pass over the doubled array to find the next greater elements.
- **Space Complexity**: \(O(n)\), for the stack used to store indices of elements in the array.

#### Code implementation in python

`O(n^2)`

```python
# Function to print element and NGE pair for all elements of list
def printNGE(arr):

    for i in range(0, len(arr), 1):

        next = -1
        for j in range(i+1, len(arr), 1):
            if arr[i] < arr[j]:
                next = arr[j]
                break

        print(str(arr[i]) + " -- " + str(next))


# Driver program to test above function
arr = [11, 13, 21, 3]
printNGE(arr)


```

`O(n)`

```python
def printNGE(arr):
    stack = []  # Initialize stack as a list

    # Dictionary to store the next greater element for each element in arr
    nge_dict = {}

    # Iterate through each element in the array
    for num in arr:
        # While stack is not empty and the top element is less than the current element
        while stack and stack[-1] < num:
            nge_dict[stack.pop()] = num
        stack.append(num)

    # For remaining elements in stack, there is no next greater element
    while stack:
        nge_dict[stack.pop()] = -1

    # Print next greater elements
    for num in arr:
        print(f"{num} -- {nge_dict[num]}")

# Driver program to test above function
arr = [11, 13, 21, 3]
printNGE(arr)
```

#### Code Implementation in C++

```cpp
#include <iostream>
#include <vector>
#include <stack>
using namespace std;

vector<int> nextGreaterElements(vector<int>& nums) {
    int n = nums.size();
    vector<int> result(n, -1); // Initialize result array with -1
    stack<int> st; // Stack to store indices
    
    // Double the array to handle circular nature
    for (int i = 0; i < 2 * n; ++i) {
        int num = nums[i % n];
        while (!st.empty() && nums[st.top()] < num) {
            result[st.top()] = num;
            st.pop();
        }
        if (i < n) {
            st.push(i); // Store indices only for the first n elements
        }
    }
    
    return result;
}

// Utility function to print the result
void printResult(const vector<int>& result) {
    cout << "Next Greater Elements: ";
    for (int num : result) {
        cout << num << " ";
    }
    cout << endl;
}

int main() {
    vector<int> nums = {1, 2, 1};

    vector<int> result = nextGreaterElements(nums);

    printResult(result);

    return 0;
}
```

### Explanation

- `Stack Usage:` We use a stack to track potential candidates for the next greater element as we traverse the doubled array.
- `Result Construction:` result array is initialized with `-1` and updated with the next greater elements found using the stack.
- `Handling Circular Array:` By iterating over `2 * n` elements (doubled array size), we effectively handle the circular nature by using modulo operation `(i % n)`.
