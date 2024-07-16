# Problem: String Rotation

**Problem Description:**

Given two strings `s1` and `s2`, determine if `s2` is a rotation of `s1`. A string `s2` is a rotation of `s1` if it can be obtained by rotating `s1` by any number of positions, clockwise or counterclockwise.

For example:

- Input: `s1 = "waterbottle", s2 = "erbottlewat"`
- Output: `true`

### Solution

To determine if `s2` is a rotation of `s1`, concatenate `s1` with itself (`s1 + s1`). Then check if `s2` is a substring of this concatenated string.

#### Steps

1. **Concatenation**: Form a new string by concatenating `s1` with itself (`s1 + s1`).
2. **Substring Check**: Check if `s2` is a substring of the concatenated string (`s1 + s1`).
3. **Result**: If `s2` is found as a substring, then `s2` is a rotation of `s1`.

#### Time and Space Complexity

- **Time Complexity**: \(O(n)\), where \(n\) is the length of `s1`. Checking substring in a concatenated string of length \(2n\) is linear.
- **Space Complexity**: \(O(n)\), for the concatenated string (`s1 + s1`).

#### Code Implementation in Python

```python
def isRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    s1s1 = s1 + s1
    
    return s2 in s1s1

# Utility function to print the result
def printResult(result):
    print("Is s2 a rotation of s1? " + ("true" if result else "false"))

if __name__ == "__main__":
    s1 = "waterbottle"
    s2 = "erbottlewat"

    result = isRotation(s1, s2)

    printResult(result)

```

#### Code Implementation in C++

```cpp
`#include <iostream>
#include <string>
using namespace std;

bool isRotation(string s1, string s2) {
    if (s1.length() != s2.length()) {
        return false;
    }
    
    string s1s1 = s1 + s1;
    
    return s1s1.find(s2) != string::npos;
}

// Utility function to print the result
void printResult(bool result) {
    cout << "Is s2 a rotation of s1? " << (result ? "true" : "false") << endl;
}

int main() {
    string s1 = "waterbottle";
    string s2 = "erbottlewat";

    bool result = isRotation(s1, s2);

    printResult(result);

    return 0;
}`
```

### Explanation

- `Concatenation:` `s1s1` is formed by concatenating `s1` with itself (`s1 + s1`).
- `Substring Search:` Use the `find` function to check if `s2` exists as a substring within `s1s1`.
- `Result:` Return `true` if `s2` is found as a substring, indicating that `s2` is a rotation of `s1`.
