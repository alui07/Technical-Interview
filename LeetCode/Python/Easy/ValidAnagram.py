""" 242. Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        anagramDict = {}
        for i in range(0, len(s)):
            if s[i] not in anagramDict:
                anagramDict[s[i]] = 1;
            else:
                anagramDict[s[i]] += 1;
        for i in range(0, len(t)):
            if t[i] not in anagramDict:
                return False;
            elif anagramDict[t[i]] == 1:
                del anagramDict[t[i]];
            else:
                anagramDict[t[i]] -= 1;
        return len(anagramDict) == 0;

