""" 15. 3Sum
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
import sys;

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        c, result = {}, [];
        for i in range(0, len(nums)):
            if (c.get(nums[i]) != None): #element already exists
                c.get(nums[i]).append(i);
            else:
                c[nums[i]] = [i];

        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                
                compliment = (nums[i] + nums[j]) * -1;
                complimentArr = c.get(compliment)
                if (complimentArr == None): continue;
                else:
                    for k in range (0, len(complimentArr)):
                        if (complimentArr[k] != i and complimentArr[k] != j and not(Solution.checkDup(self, compliment, nums[i], nums[j], result))):
                            result.append([compliment, nums[i], nums[j]]);
                            break;
        if (c.get(0) is not None and len(c.get(0)) > 2 and [0,0,0] not in result):
            result.append([0,0,0]);
        return result;
    
    def checkDup(self, a, b, c, solutions):
        for i in range(0, len(solutions)):
            if (all(x in solutions[i] for x in [a,b,c])):
                return True;
        return False;


if __name__ == '__main__':
    main(sys.argv[1:]);