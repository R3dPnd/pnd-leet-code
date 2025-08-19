# Definition for a binary tree node.
import math

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def bfs(curr: Optional[TreeNode], min, max):
            if not curr:
                return True
            # check node validity
            if curr.val <= min or curr.val >= max:
                return False
            else:
                return bfs(curr.left, min, curr.val) and bfs(curr.right, curr.val, max)
        return bfs(root, -math.inf, math.inf)