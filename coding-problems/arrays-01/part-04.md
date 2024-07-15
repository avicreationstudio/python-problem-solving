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
```

### Explanation

- `Candidate Selection:` Start with the first element as the candidate `(candidate = nums[0])` and initialize a counter `(count = 0)`.
- `Vote Counting:` Iterate through the array. If the counter is zero, update the candidate. Increment or decrement the counter based on whether the current element matches the candidate.
- `Validation:` After completing the iteration, the candidate variable holds the majority element.
