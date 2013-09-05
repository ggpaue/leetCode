/**
 * 
 * The n-queens puzzle is the problem of placing n queens on an n�n chessboard such that no two queens attack each other.
 *
 * Given an integer n, return all distinct solutions to the n-queens puzzle.
 * 
 *Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
 *
 * For example,
 * There exist two distinct solutions to the 4-queens puzzle:
 *
 * [
 *  [".Q..",  // Solution 1
 *   "...Q",
 *   "Q...",
 *   "..Q."],
 *
 *  ["..Q.",  // Solution 2
 *   "Q...",
 *   "...Q",
 *   ".Q.."]
 * ]
 * 
 */

import java.util.*;
public class Solution {
	public ArrayList<String[]> solveNQueens(int n) {
		
		ArrayList<String[]> result = new ArrayList<String[]>();
		
		solveNQueens(0, new int[n], result);
		
		return result;	
	}
	
	public void solveNQueens(int curr, int[] row, ArrayList<String[]> result) {
		int n = row.length;
		if(curr == n) {
			result.add(generateSol(row));
		} else {
			for(int i = 0; i < n; i++) {
				boolean flag = true;
				row[curr] = i;
				for(int j = 0; j < curr; j++) {
					if(row[curr] == row[j] || curr - row[curr] == j - row[j] || curr + row[curr] == j + row[j]) {
						flag = false;
						break;
					}
				}
				if(flag) {
					solveNQueens(curr + 1, row, result);
				}
			}
		}
		
	}
	
	public String[] generateSol(int[] row) {
		int n = row.length;
		String[] sol = new String[n];
		for(int i = 0; i < n; i++) {
			String line = "";
			for(int j = 0; j < n; j++) {
				if(j == row[i]) {
					line += "Q";
				} else {
					line += ".";
				}
			}
			sol[i] = line;
		}
		return sol;
	}

}
