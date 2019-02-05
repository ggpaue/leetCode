/**
 * 
 * Follow up for N-Queens problem.
 * 
 * Now, instead outputting board configurations, return the total number of distinct solutions.
 * 
 */
import java.lang.Math;
public class Solution {
	public int totalNQueens(int n) {
		assert(n > 0);
		return countSolution(1, new int[n]);
	}
	
	public int countSolution(int k, int[] pattern) {
		int n = pattern.length;
		assert(k <= n);
		int result = 0;
		main:
			for(int i = 0; i < n; i++) {
				for(int j = 0; j < k - 1; j++) {
					if(pattern[j] == i || Math.abs(j - k + 1) == Math.abs(pattern[j] - i))
						continue main;
				}
				pattern[k - 1] = i;
				if(k == n) {
					return 1;
				} else {
					result += countSolution(k + 1, pattern);
					
				}
			}
		return result;
	}

}
