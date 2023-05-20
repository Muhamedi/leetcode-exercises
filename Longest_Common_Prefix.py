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
