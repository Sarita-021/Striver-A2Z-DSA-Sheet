'''Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.'''

from collections import defaultdict
from typing import List

def valid_Row_Col(r):
    digits_cnt = defaultdict(int)
    for i in range(len(r)):
        if r[i] == '.':
            continue
        digits_cnt[r[i]] += 1
    
    for cnt in digits_cnt.values():
        if cnt > 1 :
            return False
    return True


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        print([[False] * 9 for _ in range(9)])
        for r in range(9):
            row_valid = valid_Row_Col(board[r])
            col_valid = valid_Row_Col([row[r] for row in board])

            if row_valid == False or col_valid == False:
                return False

        for row in range(0, 9, 3):  
            for col in range(0, 9, 3):  
                submatrix = []
                for r in range(row, row + 3):
                    submatrix.extend(board[r][col:col + 3]) 
                submat_valid = valid_Row_Col(submatrix) 
                if submat_valid == False : 
                    return False

        return True