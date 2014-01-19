/**
 * 
 * @author GGPAUE
 * Implement atoi to convert a string to an integer.
 * 
 * Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
 * 
 * Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
 *
 *
 */

public class Solution {
	public int atoi(String str) {
		if(str.equals("")) return 0;
		
		int position = 0;
		int result = 0;
		long val = 0L;
		char flag = '+';
		
		
		str = str.trim();
		// signed number
		if(str.charAt(0) == '+' || str.charAt(0) == '-') {
			position++;
			flag = str.charAt(0);
		}
		
		// count valid number
		while(position < str.length() && str.charAt(position) >= '0' && str.charAt(position) <= '9') {
			val = val * 10 + (str.charAt(position) - '0');
			position++;
		}
		
		if(flag == '-') val = -val;
		
		//overflow
		if(val > Integer.MAX_VALUE) {
			result = Integer.MAX_VALUE;
		} else if(val < Integer.MIN_VALUE) {
			result = Integer.MIN_VALUE;
		} else {
			result = (int)val;
		}
		
		return result;
	}

}
