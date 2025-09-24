class Solution(object):
    def myAtoi(self, s):
        
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        
        # Step 1: Trim leading whitespace
        s = s.lstrip()
        if not s:
            return 0
        
        # Step 2: Handle sign
        sign = 1
        if s[0] in ['-', '+']:
            if s[0] == '-':
                sign = -1
            s = s[1:]
        
        # Step 3: Convert digits
        result = 0
        for char in s:
            if not char.isdigit():
                break
            result = result * 10 + int(char)
        
        # Step 4: Apply sign
        result *= sign
        
        # Step 5: Clamp to 32-bit range
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
