""" 387. First Unique Character in a String
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return -1;
        if len(s) == 1: return 0;
        chars = {}
        
        for i in range(0, len(s)):
            if s[i] in chars:
                chars[s[i]] = sys.maxsize
            else:
                chars[s[i]] = i
        return min(chars.values()) if min(chars.values()) != sys.maxsize else -1;