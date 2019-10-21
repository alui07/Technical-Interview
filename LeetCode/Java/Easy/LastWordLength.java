/* 58. Length of Last Word
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5
*/
class Solution {
    public int lengthOfLastWord(String s) {
        String[] split = s.split(" ");
        if (split.length == 0) return 0;
        return split[split.length-1].length();
    }
}