# Problem: Next Greater Element II

**Problem Description:**

Given a circular array `nums` (the next element of the last element is the first element of the array), find the Next Greater Number for every element. The Next Greater Number of a number `x` is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output `-1` for this number.

For example:

- Input: `nums = [1, 2, 1]`
- Output: `[2, -1, 2]`
- Explanation:
  - For `nums[0] = 1`, the next greater number is `2`.
  - For `nums[1] = 2`, there is no greater number to its right, so we return `-1`.
  - For `nums[2] = 1`, the next greater number is `2` (circularly).

### Solution

To solve this problem efficiently, we can modify the approach using a stack-based method similar to the previous problem, but considering the circular nature of the array.

#### Steps

1. **Double the Array**: Concatenate the array with itself to handle the circular property without explicitly looping back.
2. **Stack Usage**: Use a stack to find next greater elements in the doubled array.
3. **Result Construction**: Iterate through the original array and use results from the stack to build the final result.

#### Time and Space Complexity

- **Time Complexity**: \(O(n)\), where \(n\) is the size of the array `nums`. We make a single pass over the doubled array to find the next greater elements.
- **Space Complexity**: \(O(n)\), for the stack used to store indices of elements in the array.

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
