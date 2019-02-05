/**

 * A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

 * The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

 * How many possible unique paths are there?
 * Note: m and n will be at most 100.

**/

public class Solution {
    int record[][] = new int[101][101];
	public int uniquePaths(int m, int n) {
		if(m == 0 || n == 0) return 0;
        
		if(record[m][n] != 0) return record[m][n];
		if(m == 1 || n == 1){
			return 1;
		} else {
			int subx = uniquePaths(m-1, n);
			int suby = uniquePaths(m, n-1);
			record[m][n] = subx + suby;
			return record[m][n];
		}
	}

}
