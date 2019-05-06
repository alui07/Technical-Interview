public class RomantoInteger{
	public static void main(String[] args) {
		romanToInt("III");
	}
	public static int romanToInt(String s) {
		char[] charArr = s.toCharArray();
		int result = 0;
		boolean prefix = false;
		for (int i = 0; i < s.length(); i++) {
			System.out.println();
			switch(charArr[i]) {
				case 'I':
					System.out.println("I");
					result += 1;
					prefix = true;
					break;
				case 'V':
					System.out.println("V");
					if(prefix && i > 0 && charArr[i-1] == 'I') {
						result += 3;
						prefix = false;
					} else{
						result += 5;
					}
					break;
				case 'X':
					System.out.println("X");
					if(prefix && i > 0 && charArr[i-1] == 'I') {
						result += 8;
						prefix = false;
					} else{
						result += 10;
						prefix = true;
					}
					break;
				case 'L':
					System.out.println("L");
					if (prefix && i > 0 && charArr[i-1] == 'X'){
						result += 30;
						prefix = false;
					} else {
						result += 50;
					}
					break;
				case 'C':
					System.out.println("C");
					if (prefix && i > 0 && charArr[i-1] == 'X') {
						result += 80;
						prefix = false;
					} else {
						result += 100;
						prefix = true;
					}
					break;
				case 'D':
					System.out.println("D");
					if (prefix && i > 0 && charArr[i-1] == 'C') {
						result += 300;
						prefix = false;
					} else {
						result += 500;
					}
					break;
				case 'M':
					System.out.println("M");
					if (prefix && i > 0 && charArr[i-1] == 'C') {
						result += 800;
						prefix = false;
					} else {
						result += 1000;
					}
					break;
			}
		}
		return result;
	}
}