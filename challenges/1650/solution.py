# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        p_ancestors = set()

        p_parent = p
        while p_parent:
            p_ancestors.add(p_parent.val)
            p_parent = p_parent.parent
        q_parent = q
        while q_parent:
            if q_parent.val in p_ancestors:
                return q_parent
            q_parent = q_parent.parent