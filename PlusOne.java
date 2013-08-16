/* 
 * Given a number represented as an array of digits, plus one to the number.
 *
 *
 */
public class Solution {
	public int[] plusOne(int[] digits) {
		int carry = 1;
		for(int i = digits.length - 1; i >= 0; i--) {
			if(carry == 0) break;
			if(digits[i] == 9) {
				digits[i] = 0;
			} else {
				digits[i]++;
				carry = 0;
			}
		}
		if(carry == 0) return digits;
		int[] array = new int[digits.length + 1];
		array[0] = 1;
		for(int i = 0; i < digits.length; i++) {
			array[i+1] = digits[i];
			return array;
		}
	}
	

}
