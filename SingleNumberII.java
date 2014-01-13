/*
 * 
 * Given an array of integers, every element appears three times except for one. Find that single one.
 * 
 * Note:
 * Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
 */

public class Solution {
	public int singleNumber(int[] A) {
		if(A.length == 0) return 0;
		
		int[] counts = new int[32];
		int result = 0;
		for(int i = 0; i < A.length; i++) {
			for(int j = 0; j < 32; j++) {
				if((A[i] >> j & 1) == 1) {
					counts[j] = (counts[j] + 1) % 3;
				}
			}
		}
		for(int i = 0; i < 32; i++) {
			result += (counts[i] << i);
		}
		return result;
	}
}
