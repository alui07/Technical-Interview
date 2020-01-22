""" 36. Valid Sudoku
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:

Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true
Example 2:

Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows
        #numberFreq = {}
        for row in range(len(board)):
            numberFreq = {}
            for col in range(len(board[row])):
                if board[row][col] == ".": continue
                if board[row][col] not in numberFreq: numberFreq[board[row][col]] = 1
                else: return False
            #numberFreq.clear()
        
        # check columns
        for col in range(len(board[0])):
            numberFreq = {}
            for row in range(len(board)):
                if board[row][col] == ".": continue
                if board[row][col] not in numberFreq: numberFreq[board[row][col]] = 1
                else: return False
            #numberFreq.clear()
            
        # check sub-boxes
        for i in range(9):
            # i/3 -> 0,1,2 (0, 3, 6) signify different sub-box rows
            # i%3 -> 0,1,2 signify different sub-box columns
            numberFreq = {}
            subBoxRow, subBoxCol = int(i/3), i%3
            for row in range(subBoxRow * 3, subBoxRow * 3 + 3):
                for col in range(subBoxCol * 3, subBoxCol * 3 + 3):
                    
                    if board[row][col] == ".": continue
                    if board[row][col] not in numberFreq: numberFreq[board[row][col]] = 1
                    else: return False
            #numberFreq.clear()
        return True