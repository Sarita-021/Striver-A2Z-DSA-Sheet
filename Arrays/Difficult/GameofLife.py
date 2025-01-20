'''The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or
dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the 
following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every 
cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

https://leetcode.com/problems/game-of-life/'''


from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                liveCnt = 0
                dirs = [[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
                for r, c in dirs:
                    nr, nc = i+r, j+c
                    if 0 <= nr < m and 0 <= nc < n and abs(board[nr][nc]) == 1:
                        liveCnt += 1

                if board[i][j] == 1:
                    if liveCnt < 2 or liveCnt > 3:
                        board[i][j] = -1
                else:
                    if liveCnt == 3:
                        board[i][j] = 2

        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:    board[i][j] = 1
                elif board[i][j] == -1: board[i][j] = 0  
        
        