""" 49. Group Anagrams
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

# can change anagramize to use a bit manipulation algorithm
# a word is an anagram of another word if their XOR == 0.
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        dicts, output = [], [];
        for i in range(0, len(strs)):
            countDict = self.anagramize(strs[i])
            if countDict in dicts:
                insertionIndex = dicts.index(countDict)
                output[insertionIndex].append(strs[i])
            else:
                dicts.append(countDict)
                output.append([strs[i]])
        dicts = []
        return output
    
    def anagramize(self, s):
        countDict = {}
        for i in range(0, len(s)):
            if s[i] not in countDict:
                countDict[s[i]] = 1
            else:
                countDict[s[i]] += 1
        return countDict
    