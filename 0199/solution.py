# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        levels = []

        def dfs(curr: Optional[TreeNode], level):
            if not curr:
                return
            nonlocal levels
            if len(levels) == level:
                levels.append([])
            levels[level].append(curr.val)
            dfs(curr.left, level+1)
            dfs(curr.right, level+1)

        dfs(root, 0)
        result = []
        for level in levels:
            result.append(level[-1])
        return result