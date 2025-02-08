'''Consider a rat placed at position (0, 0) in an n x n square matrix mat. The rat's goal is to reach the destination 
at position (n-1, n-1). The rat can move in four possible directions: 'U'(up), 'D'(down), 'L' (left), 'R' (right).
The rat cannot go outside the matrix and cannot move on the diagonal. The rat can only move to positions without obstacles.
Return all possible unique paths the rat can take to reach the destination. You can return the path as a string of directions
joined by hyphens (-).
If there is no way the rat can reach the destination, return an empty list.
https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1'''

from typing import List

#   Optimized solution
class Solution:
    def findPath(self, mat: List[List[int]]) -> List[str]:
        if not mat or mat[0][0] == 0 or mat[-1][-1] == 0:
            return []  # If start or end is blocked, return empty

        res = []
        n = len(mat)
        
        # Possible moves: Down, Left, Right, Up
        directions = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]
        
        def solve(row, col, path):
            # If destination is reached, store the path
            if row == n - 1 and col == n - 1:
                res.append(path)
                return

            # Mark as visited
            mat[row][col] = 0  # Block the cell

            for dx, dy, move in directions:
                newRow, newCol = row + dx, col + dy
                
                if 0 <= newRow < n and 0 <= newCol < n and mat[newRow][newCol] == 1:
                    solve(newRow, newCol, path + move)

            # Unmark (Backtrack)
            mat[row][col] = 1

        solve(0, 0, "")
        return res


# Less optimized solution
class Solution:
    # Function to find all possible paths
    def findPath(self, mat):
        res = []
        n = len(mat)
        vis = [[0 for _ in range(n)] for _ in range(n)]
        
        def solve(move, row, col, vis):
            if row == n-1 and col == n-1:
                res.append(move)
                return
            
            # Down
            if row+1 < n and not vis[row + 1][col] and mat[row+1][col] == 1:
                vis[row][col] = 1
                solve(move + 'D', row+1, col, vis)
                vis[row][col] = 0
            
            # Left
            if col-1 >= 0 and not vis[row][col-1] and mat[row][col-1] == 1:
                vis[row][col] = 1
                solve(move + 'L', row, col-1, vis)
                vis[row][col] = 0
            
            #Right
            if col+1 < n and not vis[row][col+1] and mat[row][col+1] == 1:
                vis[row][col] = 1
                solve(move + 'R', row, col+1, vis)
                vis[row][col] = 0
            
            #Up
            if row-1 >= 0 and not vis[row - 1][col] and mat[row-1][col] == 1:
                vis[row][col] = 1
                solve(move + 'U', row-1, col, vis)
                vis[row][col] = 0
                
        if mat[0][0] == 1:
            solve('', 0, 0, vis)
        
        return res
