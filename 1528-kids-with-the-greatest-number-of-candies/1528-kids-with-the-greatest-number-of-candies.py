class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        maxCandy = max(candies)
        return [(c + extraCandies) >= maxCandy for c in candies]
        