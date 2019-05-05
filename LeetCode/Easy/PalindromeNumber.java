public class PalindromeNumber{
	public static void main(String[] args) {

	}
	public boolean isPalindrome(int x) {
        if (x < 0) return false;
        char[] charArr = Integer.toString(x).toCharArray();
        for (int i = 0; i < charArr.length/2 + 1; i++) {
        	if (charArr[i] != charArr[charArr.length-1-i]) return false;
        }
        return true;
    }
}