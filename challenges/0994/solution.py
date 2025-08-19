from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        
        fresh_counter = 0
        rows, columns = len(grid), len(grid[0])

