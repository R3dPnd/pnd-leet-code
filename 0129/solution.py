# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(curr: Optional[TreeNode], val):
            if not curr:
                print(int(val))
                return int(val)
            val += str(curr.val)
            return dfs(curr.right, val) + dfs(curr.left, val)
        return dfs(root, "")