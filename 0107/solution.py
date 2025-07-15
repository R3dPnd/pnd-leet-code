# Definition for a binary tree node.
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:

        result = []

        def dfs(curr: Optional[TreeNode], level):
            nonlocal result
            if not curr:
                return

            if len(result) == level:
                result.append([])

            result[level].append(curr.val)

            if curr.left:
                dfs(curr.left, level + 1)
            if curr.right:
                dfs(curr.right, level + 1)
            
        dfs(root, 0)
        return result[::-1]