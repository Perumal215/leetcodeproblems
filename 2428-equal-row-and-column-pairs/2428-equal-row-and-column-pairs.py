class Solution(object):
    def equalPairs(self, grid):
        n = len(grid)
        row_map = {}

        for row in grid:
            key = tuple(row)
            row_map[key] = row_map.get(key, 0) + 1

        count = 0
        for c in range(n):
            col = tuple(grid[r][c] for r in range(n))
            if col in row_map:
                count += row_map[col]

        return count
