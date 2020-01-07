""" 240. Search a 2D Matrix II
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if len(matrix) == 0: return False

        # integers cannot be smaller than the current integer as you go right
        # or down.
        # increases from left to right, top to bottom, so any integers that are
        # greater than target, you can eliminate a "box" to the right and
        # downwards

        # maxX basically does that only for one dimension
        maxX = len(matrix[0])
        
        for y in range(0, len(matrix)):
            for x in range(0,maxX):
                if matrix[y][x] == target: return True
                elif target < matrix[y][x]: 
                    maxX = x
                    break
        return False