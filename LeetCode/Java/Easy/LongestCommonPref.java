/* 14. Longest Common Prefix
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
*/
public class LongestCommonPref {
	public static void main(String[] args) {
		String[] strs = new String[]{"flower", "flow", "flight"};
		System.out.println(longestCommonPrefix(strs));
	}

	public static String longestCommonPrefix(String[] strs) {
		if (strs.length == 0) return "";
		String result = "";
		char char_pref;
		for (int string_index = 0; string_index < strs[0].length(); string_index++) {
			char_pref = strs[0].charAt(string_index);
			boolean caught_exc = false;
			for (int array_index = 0; array_index < strs.length; array_index++) {
				try {
					if (strs[array_index].charAt(string_index) != char_pref) {
						return result;
					}
				} catch (Exception e) {
					caught_exc = true;
					break;
				}
			}
			if (caught_exc) {
				System.out.println("Caught exception!");

			} else {
				result += char_pref;
			}
		}

		return result;
	}
}