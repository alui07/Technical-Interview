""" 347. Top K Frequent Elements
Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

# speed: O(k*n) ~= O(n^2) --> 192ms/6.04%,15MB/100%
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 0: return None
        counterDict = {}
        result = []
        for i in range(0, len(nums)):
            if nums[i] not in counterDict:
                counterDict[nums[i]] = 1
            else:
                counterDict[nums[i]] += 1
        for i in range(0, k):
            maxVal = max(counterDict, key=counterDict.get)
            result.append(maxVal)
            counterDict.pop(maxVal)
            
        return result