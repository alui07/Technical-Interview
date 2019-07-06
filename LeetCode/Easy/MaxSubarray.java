public class MaxSubarray {
	public int maxSubArray(int[] nums) {
		int sums = 0;
    	int max = nums[0];
    	int maxSum = nums[0];

    	if (nums[0] < 0) sums = 0;
    	else sums = nums[0];

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