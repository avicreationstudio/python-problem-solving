# Problem: Valid Parentheses

**Problem Description:**

Given a string `s` containing just the characters `'(', ')', '{', '}', '['` and `']'`, determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.

For example:

- Input: `s = "()[]{}"`
- Output: `true`

- Input: `s = "([)]"`
- Output: `false`

### Solution

To solve this problem, we can use a stack data structure to keep track of the opening brackets as we iterate through the string.

#### Steps

1. **Initialization**: Use a stack to store opening brackets encountered (`'('`, `'{'`, `'['`).
2. **Iteration**: Traverse each character in the string:
   - If the character is an opening bracket (`'('`, `'{'`, `'['`), push it onto the stack.
   - If the character is a closing bracket (`')'`, `'}'`, `']'`):
     - Check if the stack is empty or the top of the stack does not match the corresponding opening bracket.
     - If either condition fails, return `false`.
     - Otherwise, pop the stack (matching opening bracket found).
3. **Completion**: After iterating through the string, check if the stack is empty. If empty, all brackets are matched correctly, otherwise, return `false`.

#### Time and Space Complexity

- **Time Complexity**: \(O(n)\), where \(n\) is the length of the string `s`. We make a single pass through the string.
- **Space Complexity**: \(O(n)\), for the stack used to store opening brackets in the worst case (when all characters are opening brackets).

#### Code Implementation in C++

```cpp
#include <iostream>
#include <stack>
#include <string>
using namespace std;

bool isValid(string s) {
    stack<char> st;
    
    for (char c : s) {
        if (c == '(' || c == '{' || c == '[') {
            st.push(c);
        } else {
            if (st.empty() || 
                (c == ')' && st.top() != '(') ||
                (c == '}' && st.top() != '{') ||
                (c == ']' && st.top() != '[')) {
                return false;
            }
            st.pop();
        }
    }
    
    return st.empty();
}

// Utility function to print the result
void printResult(bool result) {
    cout << "Is valid parentheses? " << (result ? "true" : "false") << endl;
}

int main() {
    string s1 = "()[]{}";
    string s2 = "([)]";

    bool result1 = isValid(s1);
    bool result2 = isValid(s2);

    printResult(result1);
    printResult(result2);

    return 0;
}
```

### Explanation

- `Stack Usage:` We use a stack to keep track of opening brackets encountered so far.
- `Validation Logic:` As we iterate through each character:
  - If it's an opening bracket, push it onto the stack.
  - If it's a closing bracket, check if it matches the top of the stack (matching opening bracket).
  - If not, return `false`.
- `Final Check:` After iterating through the string, ensure the stack is empty to confirm all brackets are correctly matched.
