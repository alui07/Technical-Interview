""" 859. Buddy Strings
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:

Input: A = "aa", B = "aa"
Output: true
Example 4:

Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:

Input: A = "", B = "aa"
Output: false
 

Note:

0 <= A.length <= 20000
0 <= B.length <= 20000
A and B consist only of lowercase letters.
"""
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if (len(A) != len(B)): return False;
        index1, index2 = -1, -1;
        dupeDict = {}
        for i in range(0, len(A)):
            if (A == B):
                dupeDict[A[i]] = 0
            if (A[i] != B[i]):
                if (index1 == -1):
                    index1 = i;
                elif(index2 == -1):
                    index2 = i;
                else:
                    return False;
        return (index2 != index1 and A[index1] == B[index2] and B[index1] == A[index2]) or (A==B and len(dupeDict) != len(A));