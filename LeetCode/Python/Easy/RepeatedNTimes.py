""" 961. N-Repeated Element in Size 2N Array
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3
Example 2:

Input: [2,1,2,5,3,2]
Output: 2
Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5
 

Note:

4 <= A.length <= 10000
0 <= A[i] < 10000
A.length is even
"""
class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        # all other elements are not repeated and are unique elements in the
        # list, so if you encounter a second instance of the element, return it
        count = {}
        for i in range(0, len(A)):
            if A[i] in count:
                return A[i]
            count[A[i]] = 0
        return -sys.maxsize -1