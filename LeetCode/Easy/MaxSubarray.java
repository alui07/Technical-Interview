public class MaxSubarray {
	public int maxSubArray(int[] nums) {
    	int[] sums = new int[nums.length];

    	int max = nums[0];
    	int maxForwardSum = nums[0];
    	int maxForwardIndex = 0;

    	if (nums[0] < 0) sums[0] = 0;
    	else sums[0] = nums[0];

    	for (int i = 1; i < nums.length; i++) {
    		if (sums[i-1] + nums[i] < 0) {
    			sums[i] = 0;
    		} else {
    			sums[i] = sums[i-1] + nums[i];
    		}
    		if (sums[i] > maxForwardSum) {
    			maxForwardSum = sums[i];
    			maxForwardIndex = i;
    		}
    		if (nums[i] > max) max = nums[i];
    	}

    	return (maxForwardSum == 0) ? max : maxForwardSum;
	}
}