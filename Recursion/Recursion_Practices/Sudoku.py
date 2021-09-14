
from collections import defaultdict
from copy import deepcopy

def solve_sudoku_puzzle(board):
    
    """
    Args:
     board(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    
    rows = defaultdict(set)
    cols = defaultdict(set)
    sqs = defaultdict(set)
    
    blanks = []
    
    n = len(board)
    
    for row in range(n):
        for col in range(n):
            val = board[row][col]
            if val == 0:
                blanks.append((row, col))
                continue
            
            rows[row].add(val)
            cols[col].add(val)
            sqs[(row // 3, col // 3)].add(val)
    
    def fill_blanks():
        if len(blanks) == 0:
            return True
        
        row, col = blanks.pop()
        for i in range(1, n+1):
            # element already in row
            if i in rows[row]:
                continue
            # element already in col
            if i in cols[col]:
                continue
            # element already in square
            if i in sqs[(row // 3, col // 3)]:
                continue
            
            # we can place it on the board!
            board[row][col] = i
            
            # add to sets
            rows[row].add(i)
            cols[col].add(i)
            sqs[(row // 3, col // 3)].add(i)
            
            # recurse to find other placements
            if fill_blanks():
                return True
            
            # backtrack to try other placements
            board[row][col] = 0
            rows[row].remove(i)
            cols[col].remove(i)
            sqs[(row // 3, col // 3)].remove(i)
            
        blanks.append((row, col))
            
    fill_blanks()
    
    return board




def solve_sudoku_puzzle(board):
    """
    Args:
     board(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    used_rows = {}
    used_cols = {}
    used_squares = {}
    blank_spaces = [(-1,-1)]
    
    for row in range(9):
        for col in range(9):
            used_rows[row] = []
            used_cols[col] = []
            used_squares[(row//3,col//3)] = []
            
    for row in range(9):
        for col in range(9):
            if board[row][ col] != 0:
                used_rows[row].append(board[row][col])
                used_cols[col].append(board[row][col])
                used_squares[(row//3,col//3)].append(board[row][col])
            else:
                blank_spaces.append((row,col))
    print("len of blank_spaces", len(blank_spaces))
    if len(blank_spaces) == 1:
        return
                
    def helper(row, col):
        
        if row == -1 and col == -1:
            return True
        (next_row, next_col) = blank_spaces.pop()
        
        for val in range(1, 10):
            if val in used_rows[row] or val in used_cols[col] or val in used_squares[(row//3, col//3)]:
                continue
            
            board[row][col] = val
            used_rows[row].append(val)
            used_cols[col].append(val)
            used_squares[(row//3,col//3)].append(val)
            if helper(next_row, next_col):
                return True
            
            #print("row=%d,col=%d,val=%d" %(row,col,val))
            used_squares[(row//3,col//3)].remove(val)
            used_cols[col].remove(val)
            used_rows[row].remove(val)
            board[row][col] = 0

        blank_spaces.append((next_row, next_col))
        return False
        
    
    (row,col) = blank_spaces.pop()
    helper( row, col )
    return board
        
        
            
    return []
