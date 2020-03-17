""" 238. Product of Array Except Self
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftProd = Solution.leftProduct(self, nums)
        rightProd = Solution.rightProduct(self, nums, leftProd)
        return rightProd
    
    #from left to right
    def leftProduct(self, nums: List[int]) -> List[int]:
        leftProd = [1];
        for i in range(0,len(nums)-1):
            leftProd.append(leftProd[i]*nums[i])
        return leftProd;
    
    #from right to left
    def rightProduct(self, nums: List[int], leftProd: List[int]) -> List[int]:
        num = nums[len(nums)-1]
        for i in range(len(nums)-2,-1,-1):
            leftProd[i]*=num
            num*=nums[i]
        return leftProd;