/**
 * 
 * 
 * Given numRows, generate the first numRows of Pascal's triangle.

 * For example, given numRows = 5,
 * Return

 * [
 *     [1],
 *    [1,1],
 *   [1,2,1],
 *  [1,3,3,1],
 * [1,4,6,4,1]
 * ]
 * 
 * 
 */


import java.util.*;
public class Solution {
	public ArrayList<ArrayList<Integer>> generate(int numRows) {
		ArrayList<ArrayList<Integer>> pt = new ArrayList<ArrayList<Integer>>();
		int k = 1;
		for(int i = 0; i < numRows; i++) {
			ArrayList<Integer> r = new ArrayList<Integer>();
			for(int j = 0; j < k; j++) {
				r.add(1);
			}
			k++;
			pt.add(r);
		}
		
		for(int i = 2; i < pt.size(); i++) {
			ArrayList<Integer> prev = pt.get(i-1);
			ArrayList<Integer> current = pt.get(i);
			for(int j = 1; j < current.size() - 1; j++) {
				current.set(j, prev.get(j - 1) + prev.get(j));
			}
		}
		return pt;
	}

}
