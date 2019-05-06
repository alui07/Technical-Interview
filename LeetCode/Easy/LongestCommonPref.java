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