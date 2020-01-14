""" 62. Unique Paths
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28
"""
# O(m * n) space and time
# Basic 2D DP problem
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = []

        # fill out the m x n grid
        for y in range(n):
            grid.append([])
            for x in range(m):
                if y == 0:
                    grid[y].append(1)
                elif x == 0:
                    grid[y].append(1)

                # if you're not along the top or left side of the grid, add up
                # the number of possible paths above and to the left of the
                # current position
                else:
                    grid[y].append(grid[y][x-1] + grid[y-1][x])

        # return the bottom right value in the 2D DP grid
        return grid[n-1][m-1]