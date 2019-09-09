/* 7. Reverse Integer
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
*/
public class ReverseInteger{
	public static int reverse(int x) {
		char[] charArr;
		if (x > -1) {
        	charArr = Integer.toString(x).toCharArray();
        } else {
        	String stringx = Integer.toString(x);
        	stringx = stringx.substring(1, stringx.length());
        	charArr = stringx.toCharArray();
        }
        String result = "";
        for (int i = charArr.length - 1; i > -1; i--) {
        	result += charArr[i];
        }
 
        try{
        	if (x < 0) return Integer.parseInt("-" + result);
        	return Integer.parseInt(result);
        } catch (Exception e){
        }
        return 0;

    }
    public static void main(String[] args){
    	System.out.println(Integer.toString(reverse(-123)));
    }
}