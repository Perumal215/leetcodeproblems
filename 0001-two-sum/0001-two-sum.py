class Solution(object):
    def twoSum(self, nums, target):
 
        seen = {}  # number : index

        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i