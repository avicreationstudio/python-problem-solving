def groupAnagrams(strs):
    anagram_groups = {}

    # Group anagrams using a dictionary
    for str in strs:
        sorted_str = ''.join(sorted(str))
        if sorted_str in anagram_groups:
            anagram_groups[sorted_str].append(str)
        else:
            anagram_groups[sorted_str] = [str]

    # Convert dictionary values to result format
    result = list(anagram_groups.values())
    return result

# Utility function to print the result
def printResult(result):
    print("[")
    for group in result:
        print("  [", ", ".join(f'"{s}"' for s in group), "],")
    print("]")

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    result = groupAnagrams(strs)

    print("Grouped Anagrams:")
    printResult(result)
