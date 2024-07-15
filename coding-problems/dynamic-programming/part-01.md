# Problem: Greedy Strategies

**Problem Description:**

Greedy algorithms are strategies that make the locally optimal choice at each stage with the hope of finding a global optimum. They are often used to solve optimization problems where making a choice at each step leads to an overall optimal solution.

### Characteristics of Greedy Algorithms

1. **Greedy Choice Property**: A global optimum can be reached by selecting a local optimum at each step.
2. **Optimal Substructure**: An optimal solution to the problem contains optimal solutions to subproblems.

### Examples of Problems Solved Using Greedy Algorithms

#### 1. Activity Selection Problem

Given a set of activities with start and finish times, select the maximum number of activities that can be performed by a single person, assuming that a person can only work on one activity at a time.

#### 2. Fractional Knapsack Problem

Given weights and values of items, fill a knapsack with maximum value such that the total weight of the selected items does not exceed the capacity of the knapsack. Items can be broken into fractions to maximize the total value.

#### 3. Prim's Algorithm for Minimum Spanning Tree

Find a subset of edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized. This algorithm starts with an arbitrary vertex and adds the cheapest edge to connect the growing spanning tree to an isolated vertex.

### Advantages and Disadvantages

- **Advantages**:
  - Greedy algorithms are generally easy to understand and implement.
  - They often provide efficient solutions to problems that might otherwise be computationally expensive.

- **Disadvantages**:
  - Greedy algorithms may not always provide an optimal solution.
  - They can be difficult to design for problems that require considering future choices beyond the current step.

### Code Example (Greedy Approach)

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

// Example: Fractional Knapsack Problem
struct Item {
    int weight;
    int value;
    double ratio; // value-to-weight ratio
};

bool compareItems(Item i1, Item i2) {
    return i1.ratio > i2.ratio; // Sort items by ratio in descending order
}

double fractionalKnapsack(int capacity, vector<Item>& items) {
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
    vector<Item> items = {{10, 60, 6.0}, {20, 100, 5.0}, {30, 120, 4.0}};
    int capacity = 50;
    
    double maxTotalValue = fractionalKnapsack(capacity, items);
    
    cout << "Maximum value in Knapsack = " << maxTotalValue << endl;
    
    return 0;
}
```

### Explanation

- `Code Explanation:` The `fractionalKnapsack` function implements a greedy approach to solve the fractional knapsack problem. It sorts items based on their value-to-weight ratio in descending order and then selects items greedily until the knapsack's capacity is filled.
- `Application:` This example demonstrates how a greedy strategy can be applied to maximize the value of items placed in a knapsack without exceeding its capacity, using a locally optimal choice at each step.
