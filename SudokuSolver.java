/**
 * 
 * @author GGPAUE
 * 
 * Write a program to solve a Sudoku puzzle by filling the empty cells.

 * Empty cells are indicated by the character '.'.

 * You may assume that there will be only one unique solution.
 *
 */


public class Solution {
	static final int N = 9;
	public void solveSudoku(char[][] board) {
		solveSudoku(board, 0);
	}
	
	private boolean solveSudoku(char[][] board, int n) {
		if(n == N * N) return true;
		int x = n / N;
		int y = n % N;
		if(board[x][y] != '.') return solveSudoku(board, n + 1);
		
		
		int[] choices = new int[N];
		for(int i = 0; i < N; i++) {
			if(board[x][i] != '.') {
				choices[board[x][i] - '1'] = 1;
			}
			if(board[i][y] != '.') {
				choices[board[i][y] - '1'] = 1;
			}
			
			int xi = x / 3 * 3 + i / 3;
			int yi = y / 3 * 3 + i % 3;
			
			if(board[xi][yi] != '.') {
				choices[board[xi][yi] - '1'] = 1;
			}
		}
		
		for(int i = 0; i < N; i++) {
			if(choices[i] == 0) {
				board[x][y] = (char)('1' + i);
				if(solveSudoku(board, n + 1)) {
					return true;
				}
				board[x][y] = '.';
			}
		}
		return false;	
	}

}
