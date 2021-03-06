/* 70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
*/
class Solution {
    public int climbStairs(int n) {
        if (n < 4) return n;
        int[] stairs = new int[3];
        stairs[0] = 1; stairs[1] = 2; stairs[2] = 3;
        
        //n > 3
        for (int i = 0; i < n-3; i++) {
            int j = i % 3;
            if (j == 0) {
                stairs[j] = stairs[j+1] + stairs[j+2];
            } else if (j == 1) {
                stairs[j] = stairs[j-1] + stairs[j+1];
            } else {
                stairs[j] = stairs[j-2] + stairs[j-1];
            }
        }
        return stairs[(n-1)%3];
    }
}