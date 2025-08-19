# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(curr: Optional[TreeNode], val):
            nonlocal total
            if not curr:
                return
            if is_leaf_node(curr):
                print(val + str(curr.val))
                total += int(val + str(curr.val))
                return
            dfs(curr.left, val + str(curr.val))
            dfs(curr.right, val + str(curr.val))
        
        def is_leaf_node(node: TreeNode):
            return not node.right and not node.left
        
        dfs(root, "")
        return total