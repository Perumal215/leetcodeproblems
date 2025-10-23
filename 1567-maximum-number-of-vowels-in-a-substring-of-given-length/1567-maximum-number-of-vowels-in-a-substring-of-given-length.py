class Solution(object):
    def maxVowels(self, s, k):
        vowels = set("aeiou")      # define vowels
        count = 0                  # current vowel count in the window
        max_count = 0              # maximum vowel count found so far

        # count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                count += 1
        max_count = count

        # slide the window over the string
        for i in range(k, len(s)):
            if s[i] in vowels:     # add the new character
                count += 1
            if s[i - k] in vowels: # remove the old character
                count -= 1
            if count > max_count:
                max_count = count

        return max_count
