/**
 * 
 * @author GGPAUE
 * Reverse digits of an integer.
 *
 * Example1: x = 123, return 321
 * Example2: x = -123, return -321
 *
 */

public class Solution {
	public int reverse(int x) {
		int num = Math.abs(x);
		int rest = 0;
		while(num != 0) {
			int d = num - num / 10 * 10;
			rest = rest * 10 + d;
			num /= 10;
		}
		
		if(x < 0){
			return -rest;
		} else {
			return rest;
		}
	}

}
