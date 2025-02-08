'''The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
Given an integer n, return all distinct solutions. You may return the answer in any order. 
https://leetcode.com/problems/n-queens/description/'''


from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = ['.'*n for _ in range(n)]
        
        def solve(col, left, upperDiag, lowerDiag):
            if col == n:
                res.append(board[:])
                return
            
            for row in range(n):
                if left[row] == 0 and lowerDiag[row+col] == 0 and upperDiag[(n-1)+ (col-row)] == 0:
                    left[row] = lowerDiag[row+col] = upperDiag[(n-1)+(col-row)] = 1
                    board[row] = board[row][:col] + 'Q' + board[row][col+1:]

                    solve(col+1, left, upperDiag, lowerDiag)

                    left[row] = lowerDiag[row+col] = upperDiag[(n-1)+ (col-row)] = 0
                    board[row] = board[row][:col] + '.' + board[row][col+1:]

        leftrow = [0]*n
        upperDiagonal = [0]*(2*n-1)
        lowerDiagonal = [0]*(2*n-1)
        solve(0, leftrow, upperDiagonal, lowerDiagonal)
        return res