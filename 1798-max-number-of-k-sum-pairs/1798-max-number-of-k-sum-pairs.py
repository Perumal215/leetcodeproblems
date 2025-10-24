class Solution(object):
    def maxOperations(self, nums, k):
        from collections import Counter
        count = Counter(nums)
        ops = 0

        for num in nums:
            if count[num] > 0 and count[k - num] > 0:
                if num == k - num and count[num] < 2:
                    continue
                count[num] -= 1
                count[k - num] -= 1
                ops += 1
        return ops
