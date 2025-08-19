from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(x,y):
            if x >= len(grid) or y >= len(grid[0]) or x<0 or y<0:
                return
            curr = grid[x][y]
            if curr == "0":
                return
            grid[x][y] = "0"

            dfs(x+1, y)
            dfs(x,y+1)
            dfs(x-1, y)
            dfs(x,y-1)

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "0":
                    continue
                count += 1
                dfs(x,y)
        print(grid)
        return count