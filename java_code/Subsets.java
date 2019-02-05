/**
 * 
 * Given a set of distinct integers, S, return all possible subsets.
 *
 * Note:
 *
 * Elements in a subset must be in non-descending order.
 * The solution set must not contain duplicate subsets.
 * For example,
 * If S = [1,2,3], a solution is:
 * 
 * [
 *   [3],
 *   [1],
 *   [2],
 *   [1,2,3],
 *   [1,3],
 *   [2,3],
 *   [1,2],
 *   []
 * ]
 * 
 */

import java.util.*;
public class Solution {
	public ArrayList<ArrayList<Integer>> subsets(int[] S) {
		Arrays.sort(S);
		ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
		result.add(new ArrayList<Integer>());
		for(int i = 0; i < S.length; i++) {
			int size = result.size();
			for(int j = 0; j < size; j++) {
				ArrayList<Integer> subset = new ArrayList<Integer>(result.get(j));
				subset.add(S[i]);
				result.add(subset);
			}
		}
		return result;
	}

}
