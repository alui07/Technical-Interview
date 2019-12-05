""" 283. Move Zeroes
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""
class Solution(object):
    def moveZeroes(self, nums):
        if (len(nums) == 0):
            return nums;
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        numZeroes = 0;
        zeroIndex = -1;
        for i in range(0, len(nums)):
            if (nums[i] == 0 and zeroIndex == -1):
                zeroIndex = i;
                numZeroes += 1;
            elif (nums[i] == 0):
                numZeroes += 1;
        if (numZeroes == 0): return nums;
        
        nonZeroIndex = zeroIndex + 1;
        for i in range(zeroIndex, len(nums)-numZeroes):
            while (nonZeroIndex < len(nums)):
                if (nums[nonZeroIndex] != 0):
                    nums[i] = nums[nonZeroIndex]
                    nonZeroIndex += 1;
                    break;
                else:
                    nonZeroIndex += 1;
        for i in range(len(nums) - numZeroes, len(nums)):
            nums[i] = 0;
            
        return nums;