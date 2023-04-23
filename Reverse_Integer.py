# Language - Python
# Date solved - 23/04/2023

# - Problem description
#   Given a signed 32-bit integer x, return x with its digits reversed. 
#   If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.


# - Solution 1
# - Time Complexity O(log n)
# - Explanation: First we check the sign of the number to see if its negative or positive
#   and save it, then we multiply it by the sign so that we always get a positive number.
#   We the calculate the reverse number digit by digit in the line 13 and 14 which mathematically
#   adds each digit in the reverse order multiplying it by 10. Then we decrease the original value
#   by dividing it with 10.
#   If we have 32 for example as input, on line 13 we will get:
#   --------------------------------
#   reveresed = 0 * 10 + 32 % 10 = 2
#   x = 32 // 10 = 3
#   --------------------------------
#   Next iteration we will have:
#   --------------------------------
#   reveresed = 2 * 10 + 3 % 10 = 23
#   x = 3 // 10 = 0
#   --------------------------------
#   We then assign it the correct sign by multiplying with it and check the limits

class Solution:
    def reverse(self, x: int) -> int: 
        reversed = 0
        sign = 1 if x >= 0 else -1
        x = x * sign

        while x > 0:
            reversed = reversed * 10 + x % 10
            x = x // 10
        reversed = reversed * sign

        if reversed <= -(2**31) or reversed >= (2**31 - 1): 
            return 0
        return reversed
