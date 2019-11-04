/* 118. Pascal's Triangle
Given a non-negative integer numRows, generate the first numRows of Pascal's
triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
*/
class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> triangle = new ArrayList<>(numRows);
        if (numRows == 0) return triangle;
        List<Integer> first = new ArrayList<Integer>();
        first.add(1);
        triangle.add(first);
        if (numRows > 1) {
            for (int i = 1; i < numRows; i++) {
                List<Integer> temp = new ArrayList<Integer>();
                for (int j = 0; j <= i; j++) {
                    if (j == 0 || j == i) temp.add(1);
                    else {
                        temp.add(triangle.get(i-1).get(j-1) + triangle.get(i-1).get(j));
                    }
                }
                triangle.add(temp);
            }
        }
        return triangle;
    }
}