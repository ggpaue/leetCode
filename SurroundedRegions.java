/**
 * 
 * @author GGPAUE
 * 
 * Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

 * A region is captured by flipping all 'O's into 'X's in that surrounded region .

 * For example,

 * X X X X
 * X O O X
 * X X O X
 * X O X X
 * After running your function, the board should be:

 * X X X X
 * X X X X
 * X X X X
 * X O X X
 * 
 */


public class Solution {
	public void solve(char[][] board) {
		int rows = board.length;
		if(rows == 0) return;
		int cols = board[0].length;
		
		for(int i = 0; i < cols; i++) {
			if(board[0][i] == 'O') {
				board[0][i] = '#';
				dfs(board, 0, i);
			}
			
			if(board[rows - 1][i] == 'O') {
				board[rows - 1][i] = '#';
				dfs(board, rows - 1, i);
			}
		}
		
		for(int i = 0; i < rows; i++) {
			if(board[i][0] == 'O') {
				board[i][0] = '#';
				dfs(board, i, 0);
			}
			
			if(board[i][cols - 1] == 'O') {
				board[i][cols - 1] = '#';
				dfs(board, i, cols - 1);
			}
		}
		
		changeTo(board, 'O', 'X');
		changeTo(board, '#', 'O');
		return;
	}
	
	public void dfs(char[][] board, int row, int col) {
		if(row > 0) {
			if(board[row - 1][col] == 'O') {
				board[row - 1][col] = '#';
				dfs(board, row - 1, col);
			}
		}
		
		if(col > 0) {
			if(board[row][col - 1] == 'O') {
				board[row + 1][col] = '#';
				dfs(board, row + 1, col);
			}
		}
		
		if(col < board[0].length - 1) {
			if(board[row][col + 1] == 'O') {
				board[row][col + 1] = '#';
				dfs(board, row, col + 1);
			}
		}
		return;
	}
	
	public void changeTo(char[][] board, char from, char to) {
		for(int i = 0; i < board.length; i++) {
			for(int j = 0; j < board[0].length; j++) {
				if(board[i][j] == from) {
					board[i][j] = to;
				}
			}
		}
		return;
	}

}
