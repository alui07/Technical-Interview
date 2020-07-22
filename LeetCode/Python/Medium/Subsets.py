""" 78. Subsets
iven a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        stack = [];
        result = [[]];
        for i in range(0, len(nums)):
            stack.append((nums[i],i));
        while (len(stack) != 0):
            subset = stack.pop();
            end = subset[len(subset)-1]
            push = subset[0:len(subset)-1]
            print(push)
            # for i in range(end, len(nums)):
            #     stack.append((push,nums[i],i));
            result.append([subset]);
        return result;        