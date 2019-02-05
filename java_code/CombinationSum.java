/**
 * 
 * Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
 *
 * The same repeated number may be chosen from C unlimited number of times.
 *
 * Note:
 *
 * All numbers (including target) will be positive integers.
 * Elements in a combination (a1, a2, � , ak) must be in non-descending order. (ie, a1 ? a2 ? � ? ak).
 * The solution set must not contain duplicate combinations.
 * For example, given candidate set 2,3,6,7 and target 7, 
 * A solution set is: 
 * [7] 
 * [2, 2, 3] 
 * 
 */

import java.util.*;
public class Solution {
	public ArrayList<ArrayList<Integer>> combinationSum(int[] candidates, int target) {
		ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
		ArrayList<Integer> sol = new ArrayList<Integer>();
		Arrays.sort(candidates);
		combinationSum(candidates, 0, 0, target, result, sol);
		return result;
	}
	
	private void combinationSum(int[] candidates, int start, int sum, int target, ArrayList<ArrayList<Integer>> result, ArrayList<Integer> sol) {
		if(sum == target) {
			result.add(new ArrayList<Integer>(sol));
			return;
		}
		
		if(start > candidates.length - 1) return;
		int times = 0;
		while(true) {
			if(sum > target) {
				for(int h = 0; h < times; h++) {
					sol.remove(sol.size() - 1);
				}
				break;
			}
			
			combinationSum(candidates, start + 1, sum, target, result, sol);
			sum += candidates[start];
			sol.add(candidates[start]);
			times++;
		}
	}

}
