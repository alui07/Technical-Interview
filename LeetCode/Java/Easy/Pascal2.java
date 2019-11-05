/* 119. Pascal's Triangle II
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
*/class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> triangle = new ArrayList<Integer>();
        triangle.add(1);
        if (rowIndex == 0) return triangle;
        if (rowIndex > 0) {
            triangle.add(1);
            if (rowIndex > 1) {
                for (int i = 2; i <= rowIndex; i++) {
                    for (int j = i; j >= 1; j--) {
                        if (j == i) {
                            triangle.add(1);
                        } else {
                            triangle.set(j, triangle.get(j-1) + triangle.get(j));
                        }
                    }
                }
            }
        }
        return triangle;
    }
}