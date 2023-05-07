# Language - Python
# Date solved - 07/05/2023

# - Problem description
#   Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#   An input string is valid if:
#   Open brackets must be closed by the same type of brackets.
#   Open brackets must be closed in the correct order.
#   Every close bracket has a corresponding open bracket of the same type.

# - Solution 1
# - Time Complexity O(n) where n is the length of the input string
# - Explanation: Iterate through each character
#   If its an oppening bracket, push it to the stack
#   Else check if the stack is empty which means no matching character exists then return false
#   Or else take the element from the stack top and compare it, if it is a matching bracket with the current item
#   If the loop is completed check if the stack is empty which means its a valid parentheses string else its not.

class Solution:
    def isValid(self, s: str) -> bool:
        letters = list(s)
        stack = []
        for i in range(0, len(letters)):
            if letters[i] == '(' or letters[i] == '[' or letters[i] == '{':
                stack.append(letters[i])
            elif len(stack) == 0:
                return False
            else:
                top = stack.pop()
                if not ((letters[i] == ')' and top == '(') or
                   (letters[i] == ']' and top == '[') or
                   (letters[i] == '}' and top == '{')):
                   return False
        return len(stack) == 0
