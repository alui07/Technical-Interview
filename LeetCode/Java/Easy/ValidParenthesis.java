/* 20. Valid Parenthesis
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
*/
import java.util.*;
import java.lang.*;

public class ValidParenthesis{
	public static void main(String[] args) {
		System.out.println(isValid("]"));
	}
	public static boolean isValid(String s) {
        Deque<Character> stack = new ArrayDeque<Character>();
        char[] charArr = s.toCharArray();

        for (int i = 0; i < charArr.length; i++) {
        	if (charArr[i] == '(' || charArr[i] == '{' || charArr[i] == '[') {
        		stack.push(charArr[i]);
        	} else {
        		if (stack.size() == 0) return false;
        		char pop = stack.pop();
        		if ((pop == '(' && charArr[i] != ')') || (pop == '{' && charArr[i] != '}') || (pop == '[' && charArr[i] != ']')) return false;
        	}
        }
        if (stack.size() > 0) return false;
        return true;
    }
}