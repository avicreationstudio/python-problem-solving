# Problem: Majority Element

**Problem Description:**

Given an array `nums` of size `n`, find the majority element. The majority element is the element that appears more than `⌊ n/2 ⌋` times.

You may assume that the majority element always exists in the array.

For example:

- Input: `nums = [3, 2, 3]`
- Output: `3`

### Solution

To solve this problem efficiently, we can use Moore's Voting Algorithm, which identifies a candidate for the majority element and verifies its validity.

#### Steps

1. **Candidate Selection**: Initialize a candidate and a counter.
2. **Vote Counting**: Iterate through the array. If the counter is zero, set the current element as the candidate. Increment or decrement the counter based on whether the current element matches the candidate.
3. **Validation**: After iterating through the array, the candidate is the majority element.

#### Time and Space Complexity

- **Time Complexity**: \(O(n)\), where \(n\) is the number of elements in the array. We make a single pass through the array.
- **Space Complexity**: \(O(1)\), since the algorithm uses constant extra space.

#### code implementation in python

```python
def majorityElement(nums):
    candidate = 0
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1 
        else:
            count -= 1

    return candidate

# Utility function to print the result
def printResult(result):
    print(f"Majority Element: {result}")

if __name__ == "__main__":
    nums = [3, 2, 3]

    result = majorityElement(nums)

    printResult(result)

```
<!-- 
#### Code Implementation in C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Function to find the majority element using Moore's Voting Algorithm
int majorityElement(vector<int>& nums) {
    int candidate = 0;
    int count = 0;

    for (int num : nums) {
        if (count == 0) {
            candidate = num;
        }
        count += (num == candidate) ? 1 : -1;
    }

    return candidate;
}

// Utility function to print the result
void printResult(int result) {
    cout << "Majority Element: " << result << endl;
}

int main() {
    vector<int> nums = {3, 2, 3};

    int result = majorityElement(nums);

    printResult(result);

    return 0;
}
``` -->

### Explanation

- `Candidate Selection:` Start with the first element as the candidate `(candidate = nums[0])` and initialize a counter `(count = 0)`.
- `Vote Counting:` Iterate through the array. If the counter is zero, update the candidate. Increment or decrement the counter based on whether the current element matches the candidate.
- `Validation:` After completing the iteration, the candidate variable holds the majority element.

## Test Cases

### Test Case 1

- **Input**: `nums = [3, 2, 3]`
- **Output**: `3`
- **Explanation**: The majority element is `3` as it appears twice in the array.

### Test Case 2

- **Input**: `nums = [2, 2, 1, 1, 1, 2, 2]`
- **Output**: `2`
- **Explanation**: The majority element is `2` as it appears four times in the array.

### Test Case 3

- **Input**: `nums = [1]`
- **Output**: `1`
- **Explanation**: The majority element is `1` as it is the only element in the array.

### Test Case 4

- **Input**: `nums = [1, 1, 2, 2, 1]`
- **Output**: `1`
- **Explanation**: The majority element is `1` as it appears three times in the array.

### Test Case 5

- **Input**: `nums = [4, 4, 4, 4, 1, 2, 3, 4, 4]`
- **Output**: `4`
- **Explanation**: The majority element is `4` as it appears six times in the array.

### Test Case 6

- **Input**: `nums = [5, 5, 5, 2, 5, 3, 5, 1, 5]`
- **Output**: `5`
- **Explanation**: The majority element is `5` as it appears five times in the array.

### Test Case 7

- **Input**: `nums = [8, 8, 7, 7, 7, 7, 7, 8, 8, 7, 7]`
- **Output**: `7`
- **Explanation**: The majority element is `7` as it appears seven times in the array.
