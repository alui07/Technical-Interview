/* 53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
*/
public class MaxSubarray {
	public int maxSubArray(int[] nums) {
		int sums = 0;
    	int max = nums[0];
    	int maxSum = nums[0];

    	if (nums[0] >= 0) sums = nums[0];

    	for (int i = 1; i < nums.length; i++) {
    		if (sums + nums[i] < 0) {
    			sums = 0;
    		} else {
    			sums += nums[i];
    		}
    		if (sums > maxSum) {
    			maxSum = sums;
    		}
    		if (nums[i] > max) max = nums[i];
    	}

    	return (maxSum == 0) ? max : maxSum;
	}
}