/* 1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/
import java.util.*;
import java.lang.*;

class TwoSum {
    public static int[] twoSum(int[] nums, int target) {
    	//System.out.println(Arrays.toString(nums));
  		int[] solution = new int[2];
        Map<Integer, Integer> compliments = new HashMap<Integer, Integer>();
        for(int i = 0; i < nums.length; i++) {
        	int compliment = target - nums[i];
       		//System.out.println("num: "+Integer.toString(nums[i])+", compl: "+Integer.toString(compliment));
        	if (!compliments.containsKey(nums[i])) {
        		//System.out.println("hello" + Integer.toString(i)+ " " + Integer.toString(nums[i]));
        		compliments.put(compliment, i);
        	} else {
        		System.out.println(compliments);
        		solution[0] = compliments.get(nums[i]);
        		solution[1] = i;
        		System.out.println(Integer.toString(solution[0])+Integer.toString(solution[1]));
        		return solution;

        	}
        }
        solution[0] = -1; solution[1] = -1;
        return solution;
    }
    public static void main(String[] args) {
    	int[] nums = new int[]{2,7,11,15};
    	int target = 9;
    	twoSum(nums, target);

    }
}