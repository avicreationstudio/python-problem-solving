# Rotate Array

## Description

Given an array, rotate the array to the right by k steps, where k is non-negative.

### For example

- Input: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
- Output: [5, 6, 7, 1, 2, 3, 4]

Explanation

---

- Rotate the array to the right by 1 step: `[7, 1, 2, 3, 4, 5, 6]`
- Rotate the array to the right by 2 steps: `[6, 7, 1, 2, 3, 4, 5]`
- Rotate the array to the right by 3 steps: `[5, 6, 7, 1, 2, 3, 4]`

### Solution

There are multiple ways to solve this problem. One efficient way is to use array reversal.

    Steps:
    
    Reverse the entire array.
    Reverse the first k elements.
    Reverse the remaining n - k elements

### Time and Space Complexity

`Time complexity` : O(n) where n is the number of elements in the array. This is because each reversal operation takes O(n) time, and we do a constant number of reversals.

`Space Complexity`: O(1), since we perform the rotations in place and do not use extra space proportional to the input size.

### solution ( python )

```python
def reverse(li, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        

def rotate(li):
    # step 1
    
    

li = [1, 2, 3, 4, 5, 6, 7]
n = len(li)
k = 3 


```

### array solution ( CPP )

```CPP
#include <iostream>
using namespace std;

// Function to reverse a part of the array
void reverse(int arr[], int start, int end) {
    while (start < end) {
        int temp = arr[start];
        arr[start] = arr[end];
        arr[end] = temp;
        start++;
        end--;
    }
}

// Function to rotate the array to the right by k steps
void rotate(int arr[], int n, int k) {
    k = k % n; // In case k is greater than n
    reverse(arr, 0, n - 1);
    reverse(arr, 0, k - 1);
    reverse(arr, k, n - 1);
}

// Utility function to print the array
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int arr[] = {1, 2, 3, 4, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);
    int k = 3;

    cout << "Original array: ";
    printArray(arr, n);

    rotate(arr, n, k);

    cout << "Rotated array: ";
    printArray(arr, n);

    return 0;
}


```

### vector solution ( CPP )

```c++
#include <iostream>
#include <vector>
using namespace std;

// Function to reverse a part of the array
void reverse(vector<int>& nums, int start, int end) {
    while (start < end) {
        int temp = nums[start];
        nums[start] = nums[end];
        nums[end] = temp;
        start++;
        end--;
    }
}

// Function to rotate the array to the right by k steps
void rotate(vector<int>& nums, int k) {
    int n = nums.size();
    k = k % n; // In case k is greater than n
    reverse(nums, 0, n - 1);
    reverse(nums, 0, k - 1);
    reverse(nums, k, n - 1);
}

// Utility function to print the array
void printArray(const vector<int>& nums) {
    for (int num : nums) {
        cout << num << " ";
    }
    cout << endl;
}

int main() {
    vector<int> nums = {1, 2, 3, 4, 5, 6, 7};
    int k = 3;

    cout << "Original array: ";
    printArray(nums);

    rotate(nums, k);

    cout << "Rotated array: ";
    printArray(nums);

    return 0;
}

```
