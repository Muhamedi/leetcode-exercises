# Language - Python
# Date solved - 22/04/2023

# - Solution 1
# - Reverse the string and compare with the original
# - Time Complexity O(n)

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        reversed = num[::-1]
        return num == reversed
