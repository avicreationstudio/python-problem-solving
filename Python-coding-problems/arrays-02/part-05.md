# Problem: Anagram

**Problem Description:**

Given two strings `s` and `t`, write a function to determine if `t` is an anagram of `s`.

An anagram of a string is another string that contains the same characters, only the order of characters can be different.

For example:

- Input: `s = "anagram", t = "nagaram"`
- Output: `true`

- Input: `s = "rat", t = "car"`
- Output: `false`

### Solution

To determine if two strings are anagrams, we can use a character frequency approach. This involves counting the frequency of each character in both strings and comparing these counts.

#### Steps

1. **Character Frequency Count**: Use an array of size 26 (assuming lowercase English letters) to count occurrences of each character in both strings.
2. **Comparison**: Compare the frequency arrays of `s` and `t`. If they are identical, `t` is an anagram of `s`.
3. **Edge Case**: Early return `false` if the lengths of `s` and `t` are different.

#### Time and Space Complexity

- **Time Complexity**: \(O(n)\), where \(n\) is the length of the strings `s` and `t`. We make a single pass through each string to count characters.
- **Space Complexity**: \(O(1)\), since the frequency array is fixed size (26 for lowercase English letters).

#### Code Implementation in Python

```python
def isAnagram(s, t):
    if len(s) != len(t):
        return False
    
    count = [0] * 26  # Initialize a list to count character frequencies

    # Count frequency of characters in s
    for c in s:
        count[ord(c) - ord('a')] += 1
    
    # Decrease frequency for characters in t
    for c in t:
        count[ord(c) - ord('a')] -= 1
    
    # Check if all counts are zero
    for num in count:
        if num != 0:
            return False
    
    return True

# Utility function to print the result
def printResult(result):
    print("Are the strings anagrams? " + ("true" if result else "false"))

if __name__ == "__main__":
    s1, t1 = "anagram", "nagaram"
    s2, t2 = "rat", "car"

    result1 = isAnagram(s1, t1)
    result2 = isAnagram(s2, t2)

    printResult(result1)
    printResult(result2)

```

#### Code Implementation in C++

```cpp
#include <iostream>
#include <vector>
using namespace std;

bool isAnagram(string s, string t) {
    if (s.length() != t.length()) {
        return false;
    }
    
    vector<int> count(26, 0);
    
    // Count frequency of characters in s
    for (char c : s) {
        count[c - 'a']++;
    }
    
    // Decrease frequency for characters in t
    for (char c : t) {
        count[c - 'a']--;
    }
    
    // Check if all counts are zero
    for (int num : count) {
        if (num != 0) {
            return false;
        }
    }
    
    return true;
}

// Utility function to print the result
void printResult(bool result) {
    cout << "Are the strings anagrams? " << (result ? "true" : "false") << endl;
}

int main() {
    string s1 = "anagram", t1 = "nagaram";
    string s2 = "rat", t2 = "car";

    bool result1 = isAnagram(s1, t1);
    bool result2 = isAnagram(s2, t2);

    printResult(result1);
    printResult(result2);

    return 0;
}
```

### Explanation

- `Frequency Array:` `count` is an array of size 26 initialized to zero, where each index represents a character ('a' to 'z').
- `Counting and Comparison:`
  - First, count frequencies of characters in `s`.
  - Then, decrement frequencies of characters in `t`.
  - Finally, check if all counts in the count array are zero to confirm that `t` is an anagram of `s`.
