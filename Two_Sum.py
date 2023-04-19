# Language - Python
# Date solved - 29/04/2023

# - Solution 1
# - Compare each item with each
# - Complexity O(n pow 2)

class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        for idx in range(0, len(nums)):
            diff = target - nums[idx]
            if diff in seen:
                return [seen[diff], idx]
            else:
                seen[nums[idx]] = idx

# - Solution 2
# - Iterate through the array only once
#   save seen values in a dictionary and check the current item 
#   as well as the difference if we have seen it before
# - Complexity O(n)
		
class Solution(object):
    def twoSum(self, nums, target):
        for idx1 in range(0,len(nums)):
            for idx2 in range(idx1  +1, len(nums)):
                if nums[idx1] + nums[idx2] == target:
                    return [idx1, idx2]
