/*
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
*/
public class strStr {
	public int strStr(String haystack, String needle) {
        if (needle.length() == 0 || haystack.equals(needle)) return 0;
        if (needle.length() < haystack.length() + 1) {
        	int index = 0;
        	for (; index + needle.length()< haystack.length() + 1;index++) {
        		if (haystack.substring(index, index + needle.length()).equals(needle)) return index;
        	}
        }
        return -1;
    }
}