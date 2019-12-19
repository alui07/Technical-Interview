""" 118. Pascal's Triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0: return [];
        pascalTri = []

        # generates the first numRows of pascal's triangle
        # takes care of the first two rows
        for i in range(0, numRows):
            newRow = []
            for j in range(0, i+1):
                if j == 0 or j == i: newRow.append(1)
                else:
                    # previous row before
                    prevRow = pascalTri[i-1]
                    newRow.append(prevRow[j-1] + prevRow[j])
            pascalTri.append(newRow)
        return pascalTri