class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:[] for i in range(9)}
        columns = {i:[] for i in range(9)}
        groups = {i:[] for i in range(9)}

        # Check Rows, Columns, and Groups
        for i in range(len(board)):
            for j in range(len(board[i])):
                cell = board[i][j]
                if cell == ".":
                    continue
                
                # Calculate which group this cell belongs to
                group_idx = (i // 3) * 3 + (j // 3)
                
                # Check if cell already exists in row, column, or group
                if cell in rows[i] or cell in columns[j] or cell in groups[group_idx]:
                    return False
                
                # Add cell to respective row, column, and group
                rows[i].append(cell)
                columns[j].append(cell)
                groups[group_idx].append(cell)
        
        return True