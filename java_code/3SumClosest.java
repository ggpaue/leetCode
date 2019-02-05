/**
 * 
 * Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
 *
 *  For example, given array S = {-1 2 1 -4}, and target = 1.
 *
 *  The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
 * 
 */

import java.util.Arrays;


public class Solution {
	public int threeSumClosest(int[] num, int target) {
		if(num == null || num.length == 0) return -1;
		int result = 0;
		int minDiff = Integer.MAX_VALUE;
		Arrays.sort(num);
		for(int i = 0; i < num.length - 2; i++) {
			int first = num[i];
			int left = i + 1;
			int right = num.length - 1;
			
			while(left < right) {
				int value = first + num[left] + num[right];
				if(value == target) {
					result = value;
					return result;
				}
				
				int diff = Math.abs(value - target);
				if(diff < minDiff) {
					minDiff = diff;
					result = value;
				}
				
				if(value > target) {
					right--;
				} else if(value < target) {
					left++;
				}
			}
		}
		return result;
	}

}
