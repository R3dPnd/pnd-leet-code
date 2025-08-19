from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def dfs(curr: Optional[TreeNode]) -> List[int]:
            if not curr:
                return []
            return dfs(curr.left) + [curr.val] + dfs(curr.right)
        
        in_order = dfs(root)

        swap_vals = []

        for i in range(len(in_order)-1):
            if in_order[i] > in_order[i+1] or in_order[i] < in_order[i-1]:
                swap_vals.append(in_order[i])

        print(swap_vals)

        def dfs_swap(curr: Optional[TreeNode]):
            nonlocal swap_vals

            if curr:
                if curr.val == swap_vals[0]:
                    print(curr.val)
                    curr.val = swap_vals[1]
                if curr.val == swap_vals[1]:
                    print(curr.val)
                    curr.val = swap_vals[0]
                dfs_swap(curr.left)
                dfs_swap(curr.right)
        
        dfs_swap(root)
