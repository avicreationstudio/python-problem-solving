### Problem: Greedy Knapsack

**Problem Description:**

The Greedy Knapsack problem involves filling a knapsack with items to maximize the total value, given a knapsack capacity. Unlike the Dynamic Programming Knapsack problem, the Greedy Knapsack problem uses a greedy strategy to select items based on a specific heuristic.

### Greedy Approach

The greedy strategy for the knapsack problem involves selecting items based on their value-to-weight ratio in descending order. This approach aims to maximize the value per unit weight at each step, making it a locally optimal choice.

### Steps for Greedy Knapsack

1. **Calculate Value-to-Weight Ratio**: Compute the ratio \( \text{ratio}_i = \frac{\text{value}_i}{\text{weight}_i} \) for each item \( i \).
2. **Sort Items**: Sort items based on their value-to-weight ratio in descending order.
3. **Fill Knapsack**: Select items greedily starting from the highest ratio until the knapsack's capacity is reached or all items are considered.

### Example Code Implementation in C++

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Item {
    int weight;
    int value;
    double ratio; // value-to-weight ratio
};

bool compareItems(Item i1, Item i2) {
    return i1.ratio > i2.ratio; // Sort items by ratio in descending order
}

double greedyKnapsack(int capacity, vector<Item>& items) {
    sort(items.begin(), items.end(), compareItems);
    
    double maxValue = 0.0;
    double currentWeight = 0.0;
    
    for (Item& item : items) {
        if (currentWeight + item.weight <= capacity) {
            maxValue += item.value;
            currentWeight += item.weight;
        } else {
            double remainingCapacity = capacity - currentWeight;
            maxValue += item.ratio * remainingCapacity;
            break;
        }
    }
    
    return maxValue;
}

int main() {
    vector<Item> items = {{10, 60, 0.0}, {20, 100, 0.0}, {30, 120, 0.0}};
    int capacity = 50;
    
    // Calculate ratio for each item
    for (Item& item : items) {
        item.ratio = static_cast<double>(item.value) / item.weight;
    }
    
    double maxTotalValue = greedyKnapsack(capacity, items);
    
    cout << "Maximum value in Knapsack = " << maxTotalValue << endl;
    
    return 0;
}
```

## Explanation

- `Code Explanation:` The `greedyKnapsack` function implements the greedy approach to solve the knapsack problem. It sorts items based on their value-to-weight ratio in descending order and selects items greedily until the knapsack's capacity is filled or all items are considered.
- `Application:` This example demonstrates how a greedy strategy can be applied to maximize the value of items placed in a knapsack without exceeding its capacity, using a locally optimal choice at each step based on the value-to-weight ratio.
