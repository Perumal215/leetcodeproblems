class Solution:
    def twoSum(self ,nums , target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                temp=nums[i]+nums[j]
                if temp == target:
                    return [i,j]