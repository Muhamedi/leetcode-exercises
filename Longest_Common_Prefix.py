# Language - Python
# Date solved - 20/05/2023

# - Problem description
#   Write a function to find the longest common prefix string amongst an array of strings.
#   If there is no common prefix, return an empty string "".


# - Solution
# - Time Complexity O(log n)
# - Explanation: 
#   1. Sort the array alphabetically
#   2. Loop through the minimum length of the first and last string, because the 
#      longest common prefix could be maximum up to the full first or last string whichever is minimum length 
#   3. Compare each character of the first and last string and add it to the common prefix variable

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        sorted_array = sorted(strs)
        first = sorted_array[0]
        last = sorted_array[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return common_prefix
            common_prefix += first[i]
        return common_prefix
