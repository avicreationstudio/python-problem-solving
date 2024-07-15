# Problem: Next Greater Element I

**Problem Description:**

You are given two arrays `nums1` and `nums2` where `nums1` is a subset of `nums2`. Find all elements in `nums1` for which there is a next greater element in `nums2`.

The Next Greater Element for an element `x` in `nums1` is the first greater element to its right in `nums2`. If it does not exist, output `-1` for that element.

For example:

- Input: `nums1 = [4, 1, 2], nums2 = [1, 3, 4, 2]`
- Output: `[-1, 3, -1]`
- Explanation:
  - For `4` in `nums1`, the next greater element in `nums2` is `3`.
  - For `1` in `nums1`, the next greater element in `nums2` is `3`.
  - For `2` in `nums1`, there is no greater element to its right in `nums2`, so we output `-1`.

### Solution

To solve this problem efficiently, we can use a stack-based approach to track elements in `nums2` and find the next greater elements.

#### Steps

1. **Stack Initialization**: Use a stack to store elements from `nums2` as we iterate through it.
2. **Next Greater Element Calculation**: Iterate through `nums2` from right to left:
   - Pop elements from the stack as long as they are smaller than or equal to the current element (`nums2[i]`).
   - If there's a smaller element in the stack, it's the next greater element for `nums2[i]`.
   - Store this mapping in a hash map (`nextGreater`).
3. **Result Computation**: For each element in `nums1`, use the `nextGreater` hash map to find and store the next greater element.

#### Time and Space Complexity

- **Time Complexity**: \(O(m + n)\), where \(m\) and \(n\) are the sizes of `nums1` and `nums2` respectively. We make two passes over `nums2`, one with the stack and one to build the result for `nums1`.
- **Space Complexity**: \(O(m + n)\), for the stack and the hash map used to store next greater elements.

#### Code Implementation in C++

<!-- ```cpp
#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>
using namespace std;

vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    stack<int> st;
    unordered_map<int, int> nextGreater;
    
    // Using stack to find next greater elements in nums2
    for (int i = nums2.size() - 1; i >= 0; --i) {
        while (!st.empty() && st.top() <= nums2[i]) {
            st.pop();
        }
        nextGreater[nums2[i]] = st.empty() ? -1 : st.top();
        st.push(nums2[i]);
    }
    
    // Creating result for nums1 based on nextGreater map
    vector<int> result(nums1.size());
    for (int i = 0; i < nums1.size(); ++i) {
        result[i] = nextGreater[nums1[i]];
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
    vector<int> nums1 = {4, 1, 2};
    vector<int> nums2 = {1, 3, 4, 2};

    vector<int> result = nextGreaterElement(nums1, nums2);

    printResult(result);

    return 0;
}
``` -->

```python

def fn(nums1, nums2):
    stack = []
    nextGreater = {}

    for i in range(len(nums2)-1,-1,-1):
        while len(stack) != 0 and stack[-1] <= nums2[i]:
            stack.pop()
        
        nextGreater[nums2[i]] = -1 if len(stack) == 0 else stack[-1]
        stack.append(nums2[i])
    
    result = []
    print(nextGreater)
    for x in nums1:
        result.append(nextGreater[x])
    
    return result

nums1 = [4,1,2]
nums2 = [1,3,4,2]
result = fn(nums1,nums2)
print(*result)
```

### Explanation

- `Stack Usage:` We use a stack to track potential candidates for the next greater element in nums2.
- `Hash Map:` nextGreater map stores mappings from elements in nums2 to their next greater elements.
- `Result Construction:` We iterate through nums1, using the nextGreater map to fetch and store the next greater elements or -1 if none exists.
