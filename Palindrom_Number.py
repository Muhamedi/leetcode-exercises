# Language - Python
# Date solved - 22/04/2023

# - Solution 1
# - Time Complexity O(n)
# - Explanation: Reverse the string and compare with the original

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = str(x)
        reversed = num[::-1]
        return num == reversed

# - Solution 2: Solve the problem by not converting the number to string
# - Time Complexity O(log n) 
# - Explanation: Here we construct the reversed number without converting it to a string and spliting it
#   The key to this solution is the formula "reversed = reversed * 10 + x % 10" which basically if we give it the number
#   22 for example it will give you each of the digits to the power of 10, first the number 2 then 20 which will add up to 22 reversed
#   which when comparing it with the original they will be equal hence this is a palindrome.
#   We then divide the number x by 10 so that mathematically it will remove the last digit one by one.
  
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        reversed = 0
        original = x
        while x != 0:
            reversed = reversed * 10 + x % 10
            x = x // 10
        return original == reversed
