/**
 * 
 * @author GGPAUE
 * 
 * Determine whether an integer is a palindrome. Do this without extra space.
 *
 */

public class Solution {
    public boolean isPalindrome(int x) {
		if(x < 0) return false;
		int div = 10;
		while(x / div > 9) {
			div *= 10;
		}
		while(x > 9) {
			if(x / div != x % 10) {
				return false;
			} else {
				x = x % div / 10;
				div /= 100;
			}
		}
		return true;
	}
}
