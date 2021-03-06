/**
 * 
 * @author GGPAUE
 * 
 * Given two binary strings, return their sum (also a binary string).
 *
 * For example,
 * a = "11"
 * b = "1"
 * Return "100".
 *
 */

public class Solution {
	public String addBinary(String a, String b) {
		int i = a.length() - 1;
		int j = b.length() - 1;
		int da = 0;
		int db = 0;
		int carry = 0;
		StringBuffer result = new StringBuffer();
		
		while(i >= 0 && j >= 0) {
			da = a.charAt(i--) == '0' ? 0 : 1;
			db = b.charAt(j--) == '0' ? 0 : 1;
			int d = da + db + carry;
			result.append(d % 2 == 0 ? '0' : '1');
			carry = d >> 1;
		}
		
		if(i >= 0) {
			while(i >= 0) {
				da = a.charAt(i--) == '0' ? 0 : 1;
				int d = da + carry;
				result.append(d % 2 == 0 ? '0' : '1');
				carry = d >> 1;
			}
		} else if(j >= 0) {
			while(j >= 0) {
				db = b.charAt(j--) == '0' ? 0 : 1;
				int d = db + carry;
				result.append(d % 2 == 0 ? '0' : '1');
				carry = d >> 1;
			}
		}
		
		if(carry == 1) {
			result.append('1');
		}
		
		return result.reverse().toString();
	}

}
