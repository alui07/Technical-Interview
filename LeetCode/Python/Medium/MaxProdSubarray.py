""" 152. Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example 1:

Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        leftIndex, totalProd = 0,1
        prodArray = [0]
        for i in range(len(nums)):
            if nums[i] == 0:
                prodArray.append(Solution.nonNegProd(self, nums[leftIndex:i]))
                leftIndex = i+1
        prodArray.append(Solution.nonNegProd(self, nums[leftIndex:len(nums)]))
        return max(prodArray)
    
    def nonNegProd(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        if len(nums) == 1: return nums[0]
        numNeg, totalProd = 0, 1
        for i in range(len(nums)):
            totalProd*=nums[i]
            if nums[i] < 0: numNeg+=1
        if numNeg % 2 ==0: return totalProd
        leftProd, rightProd = totalProd, totalProd
        for i in range(len(nums)-1,-1,-1):
            leftProd/=nums[i]
            if nums[i] < 0: break
        for i in range(len(nums)):
            rightProd/=nums[i]
            if nums[i] < 0: break
        return  int(leftProd) if leftProd > rightProd else int(rightProd)