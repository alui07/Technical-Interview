""" 74. Search a 2D Matrix
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
Example 1:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true
Example 2:

Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        # search for the row that has the range of elements which contain the
        # target, then search that row
        for y in range(0, len(matrix)):
            length = len(matrix[y])
            if (length > 0):
                if target == matrix[y][len(matrix[y])-1]: return True
                if target < matrix[y][len(matrix[y])-1]:
                    for x in range(0, len(matrix[y])):
                        if target == matrix[y][x]: return True
                        elif target < matrix[y][x]: return False
    
        return False