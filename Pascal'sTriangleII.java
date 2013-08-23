/**
 * 
 * Given an index k, return the kth row of the Pascal's triangle.

 * For example, given k = 3,
 * Return [1,3,3,1].

 * Note:
 * Could you optimize your algorithm to use only O(k) extra space?
 * 
 * 
 */


import java.util.*;
public class Solution {
	public ArrayList<Integer> getRow(int rowIndex) {
		
		int[] list = new int[rowIndex + 1];
		list[0] = 1;
		
		for(int j = 1; j < rowIndex + 1; j++) {
			for(int i = j - 1; i >= 1; i--) {
				list[i] = list[i - 1] + list[i];
			}
			list[j] = 1;
		}
		return getList(list);	
		
	}
	public ArrayList<Integer> getList(int[] nums) {
		ArrayList<Integer> result = new ArrayList<Integer>();
		for(int i = 0; i < nums.length; i++) {
			result.add(nums[i]);
		}
		return result;
	}

}
