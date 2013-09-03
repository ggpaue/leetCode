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
		int k = 1;
		int t = x;
		while((t = t / 10) != 0) k*= 10;
		while(x >= 10) {
			int d1 = x / k;
			int d2 = x - x / 10 * 10;
			if(d1 != d2) return false;
			x = x / 10 - d1 * (k - 1);
			k -= 2;
		}
		return true;
	}

}
