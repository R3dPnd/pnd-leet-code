# Binary Search Tree Traversal: DFS vs BFS

## Overview

Tree traversal algorithms are fundamental to working with binary search trees (BSTs) and other tree structures. Two of the most important traversal strategies are **Depth-First Search (DFS)** and **Breadth-First Search (BFS)**. Understanding the differences, use cases, and implementations of these algorithms is crucial for technical interviews and real-world applications.

## Depth-First Search (DFS)

### What is DFS?

Depth-First Search explores as far as possible along each branch before backtracking. It goes deep into the tree structure before exploring siblings.

### DFS Variants

#### 1. Inorder Traversal (Left → Root → Right)
- **Order**: Left subtree → Current node → Right subtree
- **Result**: Returns nodes in ascending order for BST
- **Use Cases**: Sorting, finding kth smallest element, validating BST

#### 2. Preorder Traversal (Root → Left → Right)
- **Order**: Current node → Left subtree → Right subtree
- **Use Cases**: Creating a copy of tree, prefix expressions, serialization

#### 3. Postorder Traversal (Left → Right → Root)
- **Order**: Left subtree → Right subtree → Current node
- **Use Cases**: Deleting tree, postfix expressions, calculating directory sizes

### DFS Implementation

```python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class DFSTraversal:
    def inorder_recursive(self, root):
        """Inorder traversal using recursion"""
        result = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)      # Visit left subtree
            result.append(node.val)  # Visit current node
            dfs(node.right)     # Visit right subtree
        
        dfs(root)
        return result
    
    def inorder_iterative(self, root):
        """Inorder traversal using stack (iterative)"""
        result = []
        stack = []
        current = root
        
        while current or stack:
            # Go to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process current node
            current = stack.pop()
            result.append(current.val)
            
            # Move to right subtree
            current = current.right
        
        return result
    
    def preorder_recursive(self, root):
        """Preorder traversal using recursion"""
        result = []
        
        def dfs(node):
            if not node:
                return
            result.append(node.val)  # Visit current node first
            dfs(node.left)      # Visit left subtree
            dfs(node.right)     # Visit right subtree
        
        dfs(root)
        return result
    
    def postorder_recursive(self, root):
        """Postorder traversal using recursion"""
        result = []
        
        def dfs(node):
            if not node:
                return
            dfs(node.left)      # Visit left subtree
            dfs(node.right)     # Visit right subtree
            result.append(node.val)  # Visit current node last
        
        dfs(root)
        return result
```

## Breadth-First Search (BFS)

### What is BFS?

Breadth-First Search explores all nodes at the current depth before moving to nodes at the next depth level. It visits nodes level by level.

### BFS Characteristics

- **Order**: Level by level, left to right
- **Data Structure**: Uses a queue (FIFO)
- **Use Cases**: Level-order traversal, finding shortest path, printing tree by levels

### BFS Implementation

```python
from collections import deque

class BFSTraversal:
    def level_order(self, root):
        """Level-order traversal using queue"""
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            # Process all nodes at current level
            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)
                
                # Add children to queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(current_level)
        
        return result
    
    def level_order_simple(self, root):
        """Simple level-order traversal (flattened result)"""
        if not root:
            return []
        
        result = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            result.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        return result
```

## Detailed Comparison

### 1. Memory Usage

| Aspect | DFS | BFS |
|--------|-----|-----|
| **Space Complexity** | O(h) where h is tree height | O(w) where w is maximum width |
| **Worst Case** | O(n) for skewed trees | O(n) for complete binary trees |
| **Memory Pattern** | Stack-based (recursion/stack) | Queue-based |

**Example**: For a skewed tree with 1000 nodes:
- DFS: Uses O(1000) space (stack depth)
- BFS: Uses O(1) space (only one level)

### 2. Time Complexity

Both algorithms have the same time complexity:
- **Time Complexity**: O(n) where n is the number of nodes
- **Each node is visited exactly once**

### 3. Traversal Order

Let's see the difference with a concrete example:

```
       1
      / \
     2   3
    / \   \
   4   5   6
```

**DFS Traversals:**
- **Inorder**: [4, 2, 5, 1, 3, 6]
- **Preorder**: [1, 2, 4, 5, 3, 6]
- **Postorder**: [4, 5, 2, 6, 3, 1]

**BFS Traversal:**
- **Level-order**: [[1], [2, 3], [4, 5, 6]] or [1, 2, 3, 4, 5, 6]

### 4. Use Cases Comparison

| Problem Type | DFS Preferred | BFS Preferred |
|--------------|---------------|---------------|
| **Path Finding** | When path length doesn't matter | When finding shortest path |
| **Tree Validation** | BST validation, symmetry | Level-based problems |
| **Tree Construction** | Serialization, copying | Level-order construction |
| **Search Problems** | Deep search, backtracking | Level-by-level search |
| **Memory Constraints** | When tree is deep but narrow | When tree is wide but shallow |

## Practical Examples

### Example 1: Finding Maximum Depth

```python
def max_depth_dfs(root):
    """Find maximum depth using DFS"""
    if not root:
        return 0
    
    left_depth = max_depth_dfs(root.left)
    right_depth = max_depth_dfs(root.right)
    
    return max(left_depth, right_depth) + 1

def max_depth_bfs(root):
    """Find maximum depth using BFS"""
    if not root:
        return 0
    
    queue = deque([(root, 1)])
    max_depth = 0
    
    while queue:
        node, depth = queue.popleft()
        max_depth = max(max_depth, depth)
        
        if node.left:
            queue.append((node.left, depth + 1))
        if node.right:
            queue.append((node.right, depth + 1))
    
    return max_depth
```

### Example 2: Path Sum Problem

```python
def has_path_sum_dfs(root, target_sum):
    """Check if path sum equals target using DFS"""
    if not root:
        return False
    
    # If leaf node, check if sum equals target
    if not root.left and not root.right:
        return target_sum == root.val
    
    # Recursively check left and right subtrees
    remaining_sum = target_sum - root.val
    return (has_path_sum_dfs(root.left, remaining_sum) or 
            has_path_sum_dfs(root.right, remaining_sum))

def has_path_sum_bfs(root, target_sum):
    """Check if path sum equals target using BFS"""
    if not root:
        return False
    
    queue = deque([(root, root.val)])
    
    while queue:
        node, current_sum = queue.popleft()
        
        # If leaf node, check if sum equals target
        if not node.left and not node.right:
            if current_sum == target_sum:
                return True
        
        # Add children with updated sums
        if node.left:
            queue.append((node.left, current_sum + node.left.val))
        if node.right:
            queue.append((node.right, current_sum + node.right.val))
    
    return False
```

## When to Use Each Algorithm

### Choose DFS when:
1. **Memory is not a constraint** and you need to explore deep paths
2. **Backtracking** is required
3. **Topological sorting** or dependency resolution
4. **Game tree exploration** (chess, tic-tac-toe)
5. **Maze solving** with recursive backtracking

### Choose BFS when:
1. **Finding shortest path** or minimum steps
2. **Level-by-level processing** is required
3. **Web crawling** (exploring links at same depth)
4. **Social network** friend suggestions
5. **GPS navigation** (finding shortest route)

## Performance Considerations

### DFS Performance Tips:
- Use **tail recursion** when possible
- Consider **iterative approach** for very deep trees
- Use **memoization** for repeated subproblems

### BFS Performance Tips:
- Use **deque** instead of list for O(1) operations
- Consider **bidirectional BFS** for path finding
- Use **visited set** to avoid cycles in graphs

## Common Interview Questions

1. **Binary Tree Level Order Traversal** (LeetCode 102)
2. **Maximum Depth of Binary Tree** (LeetCode 104)
3. **Symmetric Tree** (LeetCode 101)
4. **Path Sum** (LeetCode 112)
5. **Binary Tree Zigzag Level Order Traversal** (LeetCode 103)

## Summary

| Feature | DFS | BFS |
|---------|-----|-----|
| **Exploration Strategy** | Deep first, then backtrack | Level by level |
| **Data Structure** | Stack (recursion/iterative) | Queue |
| **Memory Usage** | O(height) | O(width) |
| **Time Complexity** | O(n) | O(n) |
| **Best For** | Deep exploration, backtracking | Shortest path, level processing |
| **Implementation** | Recursive or iterative with stack | Iterative with queue |

Understanding when to use DFS vs BFS is crucial for solving tree and graph problems efficiently. DFS is excellent for deep exploration and backtracking scenarios, while BFS shines when you need level-by-level processing or shortest path solutions.
