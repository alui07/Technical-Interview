/* 3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
*/

class Solution {
    public int lengthOfLongestSubstring(String s) {
        if (s.length() < 2) return s.length();
        for (int i = s.length(); i > -1; i--) {
            for (int j = 0; j + i < s.length()+1; j++) {
                int dupes = countDupes(s.substring(j,j+i).toCharArray());
                if (dupes == 0) return i;
                else j += dupes - 1;
            }
        }
        return 0;
    }
    
    public int countDupes(char[] arr) {
        HashMap<String, String> map = new HashMap<String, String>();
        int counter = 0;
        for (int i = 0; i < arr.length; i++) {
            if (map.containsKey("" + arr[i])) {
                counter++;
            } else {
                map.put("" + arr[i], "1");
            }
        }
        return counter;
    }
}