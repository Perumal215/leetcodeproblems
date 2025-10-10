class Solution:
    def compress(self, chars):
        write = 0
        i = 0
        n = len(chars)

        while i < n:
            char = chars[i]
            count = 1

            while i + 1 < n and chars[i] == chars[i + 1]:
                count += 1
                i += 1

            chars[write] = char
            write += 1

            if count > 1:
                for c in str(count):
                    chars[write] = c
                    write += 1

            i += 1  
        return write
