/**
 * 
 * 
 * Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

 * For example, given the following triangle

 * [
 *    [2],
 *   [3,4],
 *  [6,5,7],
 *  [4,1,8,3]
 * ]
 * The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

 * Note:
 * Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle. 
 */


import java.util.*;
public class Solution {
	public int minimumTotal(ArrayList<ArrayList<Integer>> triangle) {
		int sum = Integer.MAX_VALUE;
		int[] record = new int[1];
		record[0] = triangle.get(0).get(0);
		
		for(int i = 1; i < triangle.size(); i++) {
			ArrayList<Integer> row = triangle.get(i);
			int w = row.size();
			int[] t = new int[w];
			t[0] = record[0] + row.get(0);
			t[w-1] = record[w-2] + row.get(w-1);
			for(int j = 1; j < i; j++) {
				t[j] = row.get(j) + Math.min(record[j], record[j-1]);
			}
			
			record = (int[])t.clone();
		}
		for(int v : record) {
			sum = Math.min(sum, v);
		}
		
		return sum;
		
	}

}
