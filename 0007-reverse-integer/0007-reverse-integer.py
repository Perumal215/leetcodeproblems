class Solution(object):
    def reverse(self, x):

        INT_MIN, INT_MAX = -2**31, 2**31 - 1

        # Get the sign
        sign = -1 if x < 0 else 1
        x = abs(x)

        # Reverse using string
        rev = int(str(x)[::-1]) * sign

        # Check for 32-bit overflow
        if rev < INT_MIN or rev > INT_MAX:
            return 0
        return rev
