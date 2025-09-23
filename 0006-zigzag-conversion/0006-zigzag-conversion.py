class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        cur_row, step = 0, 1

        for ch in s:
            rows[cur_row] += ch
            if cur_row == 0:
                step = 1
            elif cur_row == numRows - 1:
                step = -1
            cur_row += step

        return "".join(rows)
