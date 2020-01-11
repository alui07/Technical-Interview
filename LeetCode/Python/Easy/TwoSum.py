""" 1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        counts = {}

        # essentially copy the list but store corresponding indeces, also check
        # if the compliment already exists in the dictionary
        for i in range(len(nums)):
            if target-nums[i] in counts: return [counts[target-nums[i]], i]
            if nums[i] not in counts: counts[nums[i]] = i
            
