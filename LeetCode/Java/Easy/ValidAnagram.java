/* 242. Valid Anagram
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
*/
class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;
        int[] sum = new int[26];
        for (int i = 0; i < s.length(); i++) {
            sum[s.charAt(i)-97]++;
            sum[t.charAt(i)-97]--;
        }
        for(int i : sum) if (i != 0) return false;
        return true;
    }
}