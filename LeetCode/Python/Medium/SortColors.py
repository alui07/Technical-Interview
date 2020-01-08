""" 75. Sort Colors
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

""" #11.8 = 28.21
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # if length = 0, nums is already sorted
        # if length = 1, nums is also already sorted
        if len(nums) < 2: return

        # the indeces represent the colors -- 0,1,2 represent red, white, and
        # blue. counts[0] represents the number of reds there are, counts[1]..
        counts = [0,0,0]

        # count the number of colors in nums
        for num in nums:
            counts[num] += 1
    
        # numIndex is an index that will iterate over the nums array
        # countIndex will iterate over the counts array
        numIndex, countIndex = 0, 0

        # iterate the entire nums array, modifying "in-place" as to not use any
        # more space
        while numIndex < len(nums):
            # check if the number of the color is 0, if it is, decrement the
            # count and modify nums 
            if counts[countIndex] != 0:
                counts[countIndex] -= 1
                nums[numIndex] = countIndex

            # otherwise find the next non-zero color, decrement the count, and
            # modify nums
            else:
                for i in range(countIndex+1, len(counts)):
                    if counts[i] != 0:
                        countIndex = i
                        break
                counts[countIndex] -= 1
                nums[numIndex] = countIndex
            numIndex += 1