/**
 * 
 * Given a collection of numbers, return all possible permutations.

 * For example,
 * [1,2,3] have the following permutations:
 * [1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1]. 
 * 
 * 
 */


import java.util.*;
public class Solution {
	public ArrayList<ArrayList<Integer>> permute(int[] num) {
		ArrayList<ArrayList<Integer>> result = new ArrayList<ArrayList<Integer>>();
		result.add(new ArrayList<Integer>());
		
		for(int i = 0; i < num.length; i++) {
			ArrayList<ArrayList<Integer>> current = new ArrayList<ArrayList<Integer>>();
			for(ArrayList<Integer> temp : result) {
				for(int j = 0; j < temp.size() + 1; j++) {
					temp.add(j, num[i]);
					ArrayList<Integer> temp1 = new ArrayList<Integer>(temp);
					current.add(temp1);
					temp.remove(j);
				}
			}
			result = new ArrayList<ArrayList<Integer>>(current);
		}
		
		return result;
	}

}
