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