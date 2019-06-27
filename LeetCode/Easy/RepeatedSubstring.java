/*
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:

Input: "abab"
Output: True
Explanation: It's the substring "ab" twice.
Example 2:

Input: "aba"
Output: False
Example 3:

Input: "abcabcabcabc"
Output: True
Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
*/
public class RepeatedSubstring {
	public boolean repeatedSubstringPattern(String s) {
		for (int i = 1; i < s.length(); i++) {
			String compare = "";
			if ((s.length() % i) == 0) {
				for (int j = 0; j < s.length()/i;j++) {
					compare += s.substring(0,i);
				}
				if (s.equals(compare)) return true;
			}
		}
        return false;
    }
}