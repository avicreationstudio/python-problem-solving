# Problem: Stock Buy Sell

**Problem Description:**

Given an array `prices` where `prices[i]` is the price of a given stock on the `i-th` day, find the maximum profit that can be achieved by buying and selling a stock at most once.

You may assume that you cannot sell a stock before you buy one.

For example:

- Input: `prices = [7, 1, 5, 3, 6, 4]`
- Output: `5`
- Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6 - 1 = 5.

### Solution

To solve this problem efficiently, we can use a single pass approach to keep track of the minimum price encountered so far and update the maximum profit as we iterate through the array.

#### Steps

1. **Initialization**: Initialize `minPrice` to a very large number and `maxProfit` to 0.
2. **Iteration**: Iterate through the array:
   - Update `minPrice` if the current price is lower than `minPrice`.
   - Update `maxProfit` if selling at the current price would yield a higher profit than previously recorded.
3. **Result**: `maxProfit` will contain the maximum profit that can be achieved by buying and selling the stock once.

#### Time and Space Complexity

- **Time Complexity**: \(O(n)\), where \(n\) is the number of elements in the array. We make a single pass through the array.
- **Space Complexity**: \(O(1)\), since the algorithm uses constant extra space.

#### Code Implementation in Python

```python
def maxProfit(prices):
    minPrice = float('inf') # this will give you infinite value
    maxProfit = 0

    for price in prices:
        if price < minPrice:
            minPrice = price
        elif (price - minPrice) > maxProfit:
            maxProfit = (price - minPrice)

    return maxProfit

# Utility function to print the result
def printResult(result):
    print(f"Maximum Profit: {result}")

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]

    result = maxProfit(prices)

    printResult(result)

```
<!-- 
#### Code Implementation in C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

// Function to find the maximum profit from stock buy sell
int maxProfit(vector<int>& prices) {
    int minPrice = INT_MAX;
    int maxProfit = 0;

    for (int price : prices) {
        if (price < minPrice) {
            minPrice = price;
        } else if (price - minPrice > maxProfit) {
            maxProfit = price - minPrice;
        }
    }

    return maxProfit;
}

// Utility function to print the result
void printResult(int result) {
    cout << "Maximum Profit: " << result << endl;
}

int main() {
    vector<int> prices = {7, 1, 5, 3, 6, 4};

    int result = maxProfit(prices);

    printResult(result);

    return 0;
}
``` -->

#### leet code

<https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/>

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float('inf')
        maxProfit = 0

        for price in prices:
            if price < minPrice:
                minPrice = price
            elif (price - minPrice) > maxProfit:
                maxProfit = (price - minPrice)
        return maxProfit
```
