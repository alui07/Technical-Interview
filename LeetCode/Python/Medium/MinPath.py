""" 64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""
class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # return 0 if grid doesn't exist
        if len(grid) == 0: return 0

        # modify grid in place, general DP solution that iterates through the 
        # entire grid. For each element, look at the previous element (above and
        # also to the left) then take the minimum and add that to the current
        # element's value. Along the edges, there is only one option instead of
        # two.
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                # if you're at the top of the grid, look left
                if y == 0 and x > 0: grid[y][x] += grid[y][x-1]

                # if you're at the left of the grid, look up
                elif x == 0 and y > 0: grid[y][x] += grid[y-1][x]

                # anywhere else, look to the left and to the right
                elif x > 0 and y > 0: grid[y][x] += min(grid[y-1][x], grid[y][x-1])
        
        # return the bottom right element
        return grid[len(grid)-1][len(grid[len(grid)-1])-1]