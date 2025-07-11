# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []

        def bfs(self, curr):
            nonlocal result
            if curr:
                bfs(self, curr.left)
                result.append(curr.val)
                bfs(self, curr.right)
            
        bfs(self, root)

        return result

    def inorderTraversalInr(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        result = []
        bfs = []

        curr = root
        while curr or bfs:
            while curr:
                bfs.append(curr)
                curr = curr.left
            curr = bfs.pop()
            result.append(curr.val)
            curr = curr.right

        return result