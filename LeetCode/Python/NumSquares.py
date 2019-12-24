""" 279. Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1: return 1
        nums, root = [1], int(math.sqrt(n))
        for i in range(1, n):
            factors = []
            
            for j in range(1, root+1):
                
                if j**2-1 == i: factors.append(1)
                    
                elif i-j**2 >= 0:
                    factors.append(nums[i-j**2] + 1)
                    
                else: break
                    
            nums.append(min(factors))
        return nums[n-1]
    
