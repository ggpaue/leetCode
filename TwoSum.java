/**
 * 
 * Given an array of integers, find two numbers such that they add up to a specific target number.
 *
 * The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
 *
 * You may assume that each input would have exactly one solution.
 *
 * Input: numbers={2, 7, 11, 15}, target=9
 * Output: index1=1, index2=2
 * 
 */

import java.util.*;
public class Solution {
	public int[] twoSum(int[] numbers, int target) {
		Map map = new HashMap<Integer, ArrayList<Integer>>();
		
		int[] result = new int[2];
		
		for(int i = 0; i < numbers.length; i++) {
			ArrayList<Integer> record;
			
			if(map.containsKey(numbers[i])) {
				record = (ArrayList<Integer>)map.get(numbers[i]);
			} else {
				record = new ArrayList<Integer>();
			}
			record.add(i);
			map.put(numbers[i], record);
		}
		
		for(int i = 0; i < numbers.length; i++) {
			int rest = target - numbers[i];
			if(map.containsKey(rest)) {
				ArrayList<Integer> record = (ArrayList<Integer>)map.get(rest);
				for(int index : record) {
					if(index != i) {
						result = new int[]{i + 1, index + 1};
						Arrays.sort(result);
						return result;
					}
				}
			}
		}
		
		return result;
	}

}
