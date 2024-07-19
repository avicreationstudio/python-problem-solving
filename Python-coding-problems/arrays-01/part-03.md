# Problem: Two Sum

**Problem Description:**

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

For example:

- Input: `nums = [2, 7, 11, 15]`, `target = 9`
- Output: `[0, 1]`
- Explanation: Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

### Solution

To solve this problem efficiently, we can use a hash table (unordered_map in C++) to store the difference between the target and each element in the array as we iterate through the array. This allows us to check in constant time whether the complement of the current element exists in the hash table.

#### Time and Space Complexity

- **Time Complexity**: \(O(n)\), where \(n\) is the number of elements in the array. We traverse the array once, and lookups in the hash table are \(O(1)\) on average.
- **Space Complexity**: \(O(n)\), due to the additional space required for the hash table.

#### python

```python
def twoSum(nums, target):
    hashTable = {}  # Hash table to store the complement and index

    for i, num in enumerate(nums):
        complement = target - num

        # Check if the complement exists in the hash table
        if complement in hashTable:
            return [hashTable[complement], i]  # Return the indices of the two numbers

        # Store the index of the current element in the hash table
        hashTable[num] = i

    # If no solution is found, return an empty list (though the problem guarantees a solution)
    return []

# Utility function to print the result
def printResult(result):
    if len(result) == 2:
        print(result[0], result[1])
    else:
        print("No solution found.")

if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    result = twoSum(nums, target)

    printResult(result)

```
<!-- 
#### cpp

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

// Function to find the two sum indices
vector<int> twoSum(int nums[], int n, int target) {
    unordered_map<int, int> hashTable; // Hash table to store the complement and index

    for (int i = 0; i < n; i++) {
        int complement = target - nums[i];

        // Check if the complement exists in the hash table
        if (hashTable.find(complement) != hashTable.end()) {
            return {hashTable[complement], i}; // Return the indices of the two numbers
        }

        // Store the index of the current element in the hash table
        hashTable[nums[i]] = i;
    }

    // If no solution is found, return an empty vector (though the problem guarantees a solution)
    return {};
}

// Utility function to print the result
void printResult(const vector<int>& result) {
    if (result.size() == 2) {
        cout << "Indices: [" << result[0] << ", " << result[1] << "]" << endl;
    } else {
        cout << "No solution found." << endl;
    }
}

int main() {
    int nums[] = {2, 7, 11, 15};
    int n = sizeof(nums) / sizeof(nums[0]);
    int target = 9;

    vector<int> result = twoSum(nums, n, target);

    printResult(result);

    return 0;
}

``` -->

### Explanation

- `Hash Table Initialization:` We initialize an empty hash table to store the indices of the array elements.
- `Iteration:` We iterate through the array, and for each element, we calculate its complement with respect to the target (complement = target - nums[i]).
- `Complement Check:` We check if the complement exists in the hash table. If it does, we have found the two indices whose elements sum up to the target, and we return these indices.
- `Hash Table Update:
- ` If the complement does not exist in the hash table, we store the current element and its index in the hash table for future reference.

## Test Cases

### Test Case 1

- **Input**: `nums = [2, 7, 11, 15]`, `target = 9`
- **Output**: `[0, 1]`
- **Explanation**: `nums[0] + nums[1] == 9`, so we return `[0, 1]`.

### Test Case 2

- **Input**: `nums = [3, 2, 4]`, `target = 6`
- **Output**: `[1, 2]`
- **Explanation**: `nums[1] + nums[2] == 6`, so we return `[1, 2]`.

### Test Case 3

- **Input**: `nums = [3, 3]`, `target = 6`
- **Output**: `[0, 1]`
- **Explanation**: `nums[0] + nums[1] == 6`, so we return `[0, 1]`.

### Test Case 4

- **Input**: `nums = [1, 2, 3, 4, 5]`, `target = 9`
- **Output**: `[3, 4]`
- **Explanation**: `nums[3] + nums[4] == 9`, so we return `[3, 4]`.

### Test Case 5

- **Input**: `nums = [0, 4, 3, 0]`, `target = 0`
- **Output**: `[0, 3]`
- **Explanation**: `nums[0] + nums[3] == 0`, so we return `[0, 3]`.
