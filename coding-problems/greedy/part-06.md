# Problem: Group Anagrams

**Problem Description:**

Given an array of strings `strs`, group the anagrams together. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

For example:

- Input: `strs = ["eat", "tea", "tan", "ate", "nat", "bat"]`
- Output: `[["ate","eat","tea"], ["nat","tan"], ["bat"]]`

### Solution

To group anagrams together efficiently, we can use a hash map where the key is a sorted version of each string (representing its canonical form), and the value is a list of strings that match this sorted form.

#### Steps

1. **Hash Map**: Use an unordered map (`unordered_map<string, vector<string>>`) to store groups of anagrams.
2. **Grouping**: Iterate through each string in `strs`:
   - Sort each string to get its canonical form.
   - Use this sorted string as a key in the hash map and append the original string to the corresponding vector.
3. **Result Construction**: Convert the values of the hash map (vectors of anagrams) into the final result list.

#### Time and Space Complexity

- **Time Complexity**: (O(n * k log k)), where (n) is the number of strings in `strs` and (k) is the maximum length of a string in `strs`. Sorting each string takes (k log k) time.
- **Space Complexity**: (O(n * k)), for storing all strings in the hash map.

#### Code Implementation in C++

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> anagramGroups;
    
    // Group anagrams using a hash map
    for (string& str : strs) {
        string sortedStr = str;
        sort(sortedStr.begin(), sortedStr.end());
        anagramGroups[sortedStr].push_back(str);
    }
    
    // Convert hash map values to result format
    vector<vector<string>> result;
    for (auto& pair : anagramGroups) {
        result.push_back(pair.second);
    }
    
    return result;
}

// Utility function to print the result
void printResult(const vector<vector<string>>& result) {
    cout << "[";
    for (const auto& group : result) {
        cout << "[";
        for (const string& str : group) {
            cout << "\"" << str << "\", ";
        }
        cout << "], ";
    }
    cout << "]" << endl;
}

int main() {
    vector<string> strs = {"eat", "tea", "tan", "ate", "nat", "bat"};

    vector<vector<string>> result = groupAnagrams(strs);

    cout << "Grouped Anagrams: ";
    printResult(result);

    return 0;
}
```

### Explanation

- `Hash Map Usage:` `anagramGroups` is used to store groups of anagrams, where the key is the sorted version of each string and the value is a vector of original strings that match this sorted form.
- `Sorting and Grouping:`
  - Iterate through each string in `strs`.
  - Sort each string to obtain its canonical form (`sortedStr`).
  - Use `sortedStr` as a key in the hash map and append the original string to the corresponding vector.
- `Result Construction:` Convert the values of `anagramGroups` into the final result format, which is a vector of vectors representing grouped anagrams.
