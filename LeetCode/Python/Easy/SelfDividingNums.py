""" 728. Self Dividing Numbers
A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
"""

class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        
        # check all numbers within the bounds of [left, right] (inclusive)
        for i in range(left, right+1):
            if self.checkSelfDivision(i): 
                result.append(i)
        return result
    
    def checkSelfDivision(self, num):
        n = num
        while n > 0:
            digit = n % 10
            # if a digit is 0, return false
            if digit == 0: 
                return False
            # check if each digit can divide into the main number, if even one
            # digit cannot, return False
            if num % digit == 0:
                n /= 10
            else: 
                return False
        return True
        