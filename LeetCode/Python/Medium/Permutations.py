""" 46. Permutations
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if (nums is None): return [];
        elif (len(nums) == 1): return [nums];
        result = []
        for option in nums:
            a = list(nums)
            a.remove(option);
            nextLevels = Solution.permute(self, a);
            for nextLevel in nextLevels:
                nextLevel.insert(0, option);
            result.extend(nextLevels);
        return result;