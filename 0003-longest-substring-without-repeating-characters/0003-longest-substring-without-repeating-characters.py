class Solution(object):
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        left = 0
        max_length = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1  # move left pointer
            last_seen[ch] = right
            max_length = max(max_length, right - left + 1)

        return max_length

