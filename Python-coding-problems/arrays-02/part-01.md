# Problem: Move Zeros to End

**Problem Description:**

Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

For example:

- Input: `nums = [0, 1, 0, 3, 12]`
- Output: `[1, 3, 12, 0, 0]`

### Solution

To solve this problem efficiently, we can use a two-pointer approach. One pointer (`i`) iterates through the array to find non-zero elements, and another pointer (`j`) keeps track of the position to place the next non-zero element.

#### Steps

1. **Initialization**: Start with two pointers, `i` at the beginning of the array and `j` at `0`.
2. **Iteration**: Traverse the array with `i`:
   - If `nums[i]` is non-zero, swap `nums[i]` with `nums[j]` and increment `j`.
3. **Completion**: After the iteration, all non-zero elements are moved to the front, and all zeros are at the end.

#### Time and Space Complexity

- **Time Complexity**: \(O(n)\), where \(n\) is the size of the array. We make a single pass through the array.
- **Space Complexity**: \(O(1)\), as the algorithm uses only a constant amount of extra space.

#### Code Implementation in Python

```python
def moveZeroes(nums):
    j = 0  # Pointer to place the next non-zero element

    # Traverse the array
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]  # Swap
            j += 1

# Utility function to print the array
def printArray(nums):
    print(" ".join(map(str, nums)))

if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]

    moveZeroes(nums)

    print("Array after moving zeros:")
    printArray(nums)

```

#### Code Implementation in C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

void moveZeroes(vector<int>& nums) {
    int j = 0; // Pointer to place the next non-zero element

    // Traverse the array
    for (int i = 0; i < nums.size(); ++i) {
        if (nums[i] != 0) {
            swap(nums[i], nums[j]);
            ++j;
        }
    }
}

// Utility function to print the array
void printArray(const vector<int>& nums) {
    for (int num : nums) {
        cout << num << " ";
    }
    cout << endl;
}

int main() {
    vector<int> nums = {0, 1, 0, 3, 12};

    moveZeroes(nums);

    cout << "Array after moving zeros: ";
    printArray(nums);

    return 0;
}
```

### Explanation

- `Initialization:` `j` starts at `0`, indicating the next position for a non-zero element.
- `Iteration and Swapping:` For each element `nums[i]`, if it's non-zero, swap it with `nums[j]`and move `j` forward.
- `Result:` After the loop, all non-zero elements are at the beginning, and zeros follow them, preserving the relative order of the non-zero elements.
