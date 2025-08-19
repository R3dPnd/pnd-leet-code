from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                if grid[x][y] == '1':
                    self.dfs(grid, x, y)
                    count += 1
        return count

    def dfs(self, grid, x, y):
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[x]) or grid[x][y] == '0':
            return