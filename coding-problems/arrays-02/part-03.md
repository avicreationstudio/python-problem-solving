# Problem: Trapping Rain Water

**Problem Description:**

Given `n` non-negative integers representing an elevation map where the width of each bar is `1`, compute how much water it can trap after raining.

For example:

- Input: `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`
- Output: `6`
- Explanation: In this case, 6 units of rain water (blue section) are being trapped.

### Solution

To solve this problem efficiently, we can use a two-pointer technique to determine the amount of water trapped between the bars.

#### Steps

#### Two-Pointer Approach

1. **Initialize Two Pointers**: Set two pointers, `left` and `right`, at the beginning and end of the elevation map.
2. **Initialize Variables**: Set `left_max` and `right_max` to track the maximum heights from the left and right pointers, respectively.
3. **Iterate and Calculate Water Trapped**:
   - Move the pointers towards each other.
   - For each position, update the `left_max` and `right_max`.
   - Calculate the water trapped based on the smaller of the two maximum heights.

#### Time and Space Complexity

- **Time Complexity**: \(O(n)\), where \(n\) is the length of the `height` array. Each element is processed at most twice.
- **Space Complexity**: \(O(1)\), since only a constant amount of extra space is used.

#### Code Implementation in C++
<!-- 
```cpp
#include <iostream>
#include <vector>
using namespace std;

int trap(vector<int>& height) {
    int n = height.size();
    if (n == 0) return 0;

    int left = 0, right = n - 1;
    int leftMax = 0, rightMax = 0;
    int water = 0;

    while (left <= right) {
        if (height[left] <= height[right]) {
            if (height[left] >= leftMax) {
                leftMax = height[left];
            } else {
                water += leftMax - height[left];
            }
            ++left;
        } else {
            if (height[right] >= rightMax) {
                rightMax = height[right];
            } else {
                water += rightMax - height[right];
            }
            --right;
        }
    }

    return water;
}

// Utility function to print the result
void printResult(int result) {
    cout << "Amount of trapped water: " << result << endl;
}

int main() {
    vector<int> height = {0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1};

    int result = trap(height);

    printResult(result);

    return 0;
}
``` -->

```python
def trap(height):
    if not height:
        return 0

    left, right = 0, len(height) - 1
    left_max, right_max = height[left], height[right]
    water_trapped = 0

    while left < right:
        if left_max < right_max:
            left += 1
            left_max = max(left_max, height[left])
            water_trapped += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water_trapped += right_max - height[right]

    return water_trapped

# Example usage
height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(f"Trapped water: {trap(height)}")
```

1. **Flat Surface**:
    - **Input**: `height = [0, 0, 0, 0, 0]`
    - **Output**: `0`
    - **Explanation**: No water can be trapped as there are no bars to form a container.

2. **Single Bar**:
    - **Input**: `height = [4]`
    - **Output**: `0`
    - **Explanation**: No water can be trapped with a single bar.

3. **Two Bars**:
    - **Input**: `height = [2, 4]`
    - **Output**: `0`
    - **Explanation**: No water can be trapped between two bars.

4. **Increasing Bars**:
    - **Input**: `height = [1, 2, 3, 4, 5]`
    - **Output**: `0`
    - **Explanation**: The water will flow off to the right, trapping no water.

5. **Decreasing Bars**:
    - **Input**: `height = [5, 4, 3, 2, 1]`
    - **Output**: `0`
    - **Explanation**: The water will flow off to the left, trapping no water.

6. **V-Shaped Valley**:
    - **Input**: `height = [3, 0, 3]`
    - **Output**: `3`
    - **Explanation**: Water is trapped in the valley between the bars.

7. **Plateau**:
    - **Input**: `height = [2, 2, 2, 2, 2]`
    - **Output**: `0`
    - **Explanation**: No water can be trapped on a flat surface.

8. **Random Peaks and Valleys**:
    - **Input**: `height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]`
    - **Output**: `6`
    - **Explanation**: Water is trapped in various valleys formed by the peaks.

9. **Edge Case with Large Numbers**:
    - **Input**: `height = [100000, 1, 100000]`
    - **Output**: `99999`
    - **Explanation**: Large amount of water is trapped in the deep valley.

10. **Alternating Heights**:
    - **Input**: `height = [1, 0, 1, 0, 1, 0, 1]`
    - **Output**: `3`
    - **Explanation**: Water is trapped between alternating peaks.

Flat Surface: There are no barriers to trap water.
Single Bar: A single bar cannot trap any water.
Two Bars: No container can be formed with just two bars.
Increasing Bars: Water flows off the right edge.
Decreasing Bars: Water flows off the left edge.
V-Shaped Valley: Water is trapped in the valley.
Plateau: A flat surface cannot trap water.
Random Peaks and Valleys: Various valleys trap water.
Edge Case with Large Numbers: A deep valley traps a large amount of water.

### Explanation

- The `while` loop runs until the `left` pointer meets the `right` pointer.
- If `left_max` is less than `right_max`, move the `left` pointer to the right.
  - Update `left_max` with the maximum height encountered so far from the left.
  - Calculate the water trapped at the current position as `left_max - height[left]`.
- If `right_max` is less than or equal to `left_max`, move the `right` pointer to the left.
  - Update `right_max` with the maximum height encountered so far from the right.
  - Calculate the water trapped at the current position as `right_max - height[right]`.
