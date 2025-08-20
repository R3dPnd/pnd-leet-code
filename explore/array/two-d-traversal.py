def traverse_2d_array(arr, direction='row'):
    """
    Traverse a 2D array either by rows or by columns.
    
    Args:
        arr (list): 2D array to traverse
        direction (str): 'row' for row-wise traversal, 'col' for column-wise traversal
    
    Returns:
        list: Traversed elements in the specified order
    """
    if not arr or not arr[0]:
        return []
    
    rows, cols = len(arr), len(arr[0])
    result = []
    
    if direction.lower() == 'row':
        # Traverse row by row
        for i in range(rows):
            for j in range(cols):
                result.append(arr[i][j])
    elif direction.lower() == 'col':
        # Traverse column by column
        for j in range(cols):
            for i in range(rows):
                result.append(arr[i][j])
    else:
        raise ValueError("Direction must be 'row' or 'col'")
    
    return result


def traverse_2d_array_with_positions(arr, direction='row'):
    """
    Traverse a 2D array and return elements with their positions.
    
    Args:
        arr (list): 2D array to traverse
        direction (str): 'row' for row-wise traversal, 'col' for column-wise traversal
    
    Returns:
        list: List of tuples (value, row, col) in traversal order
    """
    if not arr or not arr[0]:
        return []
    
    rows, cols = len(arr), len(arr[0])
    result = []
    
    if direction.lower() == 'row':
        # Traverse row by row
        for i in range(rows):
            for j in range(cols):
                result.append((arr[i][j], i, j))
    elif direction.lower() == 'col':
        # Traverse column by column
        for j in range(cols):
            for i in range(rows):
                result.append((arr[i][j], i, j))
    else:
        raise ValueError("Direction must be 'row' or 'col'")
    
    return result


def print_2d_array(arr):
    """Helper function to print a 2D array in a readable format."""
    for row in arr:
        print(row)


# Example usage and demonstrations
if __name__ == "__main__":
    print("=== 2D Array Traversal Examples ===\n")
    
    # Example 1: Simple 3x3 array
    print("Example 1: 3x3 Array")
    print("Array:")
    arr1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_2d_array(arr1)
    
    print("\nRow-wise traversal:", traverse_2d_array(arr1, 'row'))
    print("Column-wise traversal:", traverse_2d_array(arr1, 'col'))
    
    print("\nRow-wise with positions:")
    for value, row, col in traverse_2d_array_with_positions(arr1, 'row'):
        print(f"Value {value} at position ({row}, {col})")
    
    print("\nColumn-wise with positions:")
    for value, row, col in traverse_2d_array_with_positions(arr1, 'col'):
        print(f"Value {value} at position ({row}, {col})")
    
    print("\n" + "="*50 + "\n")
    
    # Example 2: 2x4 array
    print("Example 2: 2x4 Array")
    print("Array:")
    arr2 = [
        ['a', 'b', 'c', 'd'],
        ['e', 'f', 'g', 'h']
    ]
    print_2d_array(arr2)
    
    print("\nRow-wise traversal:", traverse_2d_array(arr2, 'row'))
    print("Column-wise traversal:", traverse_2d_array(arr2, 'col'))
    
    print("\n" + "="*50 + "\n")
    
    # Example 3: 4x2 array
    print("Example 3: 4x2 Array")
    print("Array:")
    arr3 = [
        [10, 20],
        [30, 40],
        [50, 60],
        [70, 80]
    ]
    print_2d_array(arr3)
    
    print("\nRow-wise traversal:", traverse_2d_array(arr3, 'row'))
    print("Column-wise traversal:", traverse_2d_array(arr3, 'col'))
    
    print("\n" + "="*50 + "\n")
    
    # Example 4: Error handling
    print("Example 4: Error Handling")
    try:
        result = traverse_2d_array(arr1, 'invalid')
    except ValueError as e:
        print(f"Error caught: {e}")
    
    # Example 5: Empty array handling
    print("\nExample 5: Empty Array Handling")
    empty_arr = []
    print("Empty array result:", traverse_2d_array(empty_arr, 'row'))
    
    # Example 6: Custom traversal with specific pattern
    print("\nExample 6: Custom Traversal Pattern")
    print("Spiral-like traversal (outer boundary first):")
    
    def spiral_traversal(arr):
        """Custom spiral traversal starting from outer boundary."""
        if not arr or not arr[0]:
            return []
        
        rows, cols = len(arr), len(arr[0])
        result = []
        
        # Top row
        for j in range(cols):
            result.append(arr[0][j])
        
        # Right column (excluding top element)
        for i in range(1, rows):
            result.append(arr[i][cols-1])
        
        # Bottom row (excluding right element, reverse order)
        if rows > 1:
            for j in range(cols-2, -1, -1):
                result.append(arr[rows-1][j])
        
        # Left column (excluding bottom and top elements, reverse order)
        if cols > 1:
            for i in range(rows-2, 0, -1):
                result.append(arr[i][0])
        
        return result
    
    print("Spiral traversal result:", spiral_traversal(arr1))
