/* 387. First Unique Character in a String
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
*/
class Solution {
    public int firstUniqChar(String s) {
        if (s.length() == 1) return 0;
        if (s.length() == 0) return -1;
        HashMap<String, Integer> map = new HashMap<String, Integer>();
        int index = s.length()-1;
        for (int i = s.length()-1; i > -1; i--) {
            if (map.containsKey(""+s.charAt(i))) {
                map.replace(""+s.charAt(i), -1);
            }
            else {
                map.put(""+s.charAt(i), i);
            }
        }
        boolean none = true;
        for (int value : map.values()) {
            if (value != -1 && value <= index) {
                index = value;
                none = false;
            }
        }
        if(none) return -1;
        return index;
    }
}