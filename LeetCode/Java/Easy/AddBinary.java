/* 67. Add Binary
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
*/
class Solution {
    public String addBinary(String a, String b) {
        int index = 1;
        boolean carryOver = false;
        StringBuilder sb = new StringBuilder();
        while (a.length() - index > -1 || b.length() - index > -1) {
            int aa = 0, bb = 0;
            if (!(index > a.length())) aa=Character.getNumericValue(a.charAt(a.length()-index));
            if (!(index > b.length())) bb=Character.getNumericValue(b.charAt(b.length()-index));
            if (carryOver) {
                aa++;
                carryOver = false;
            }

            int result = 0;
            if (aa + bb > 1) {
                carryOver = true;
                result = aa+bb-2;
            } else {
                result = aa+bb;
            }
            sb.insert(0,""+result);
            index++;
            if (carryOver && index > a.length() && index > b.length()) sb.insert(0, "1");
        }
        return sb.toString();
    }
}