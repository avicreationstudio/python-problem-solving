# Problem: Sort Colors

**Problem Description:**

Given an array `nums` with `n` objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

Here, we will use the integers `0`, `1`, and `2` to represent the color red, white, and blue respectively.

For example:

- Input: `nums = [2, 0, 2, 1, 1, 0]`
- Output: `[0, 0, 1, 1, 2, 2]`

### Solution

To solve this problem efficiently, we can use the Dutch National Flag algorithm, which partitions the array into three sections: reds (0s), whites (1s), and blues (2s).

#### Steps

1. **Initialization**: Use three pointers: `low`, `mid`, and `high`. `low` points to the beginning of the array, `mid` starts from the beginning, and `high` points to the end of the array.
2. **Partitioning**: Traverse the array with `mid`:
   - If `nums[mid]` is `0`, swap it with `nums[low]` and increment both `low` and `mid`.
   - If `nums[mid]` is `1`, just increment `mid`.
   - If `nums[mid]` is `2`, swap it with `nums[high]` and decrement `high`.
3. **Termination**: Stop when `mid` exceeds `high`, as all elements are correctly partitioned.

#### Time and Space Complexity

- **Time Complexity**: \(O(n)\), where \(n\) is the size of the array. We make a single pass through the array.
- **Space Complexity**: \(O(1)\), as the algorithm uses only a constant amount of extra space.

#### Code Implementation in C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

void sortColors(vector<int>& nums) {
    int low = 0, mid = 0;
    int high = nums.size() - 1;

    while (mid <= high) {
        if (nums[mid] == 0) {
            swap(nums[low], nums[mid]);
            ++low;
            ++mid;
        } else if (nums[mid] == 1) {
            ++mid;
        } else { // nums[mid] == 2
            swap(nums[mid], nums[high]);
            --high;
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
    vector<int> nums = {2, 0, 2, 1, 1, 0};

    sortColors(nums);

    cout << "Sorted colors array: ";
    printArray(nums);

    return 0;
}
```

### Explanation

1. `Initialization:` `low` starts at `0`, `mid` starts at `0`, and `high` starts at the end of the array.
1. `Partitioning Logic:`
    - If nums[mid] is `0`, swap it with `nums[low]` to move `0` to the beginning and increment both `low` and `mid`.
    - If nums[mid] is `1`, just move `mid` forward to keep it in place.
    - If nums[mid] is `2`, swap it with `nums[high]` to move `2` to the end and decrement `high`.
1. `Result:` After the loop, the array is sorted such that all `0`s come first, followed by all `1`s, and then all `2`s.
