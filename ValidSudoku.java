/**
 * 
 * Determine if a Sudoku is valid, according to: Sudoku Puzzles - The Rules.

 * The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
 * 
 */
import java.util.*;
public class Solution {
	public boolean isValidSudoku(char[][] board) {
		Set[] rows = new Set[9];
		Set[] cols = new Set[9];
		Set[][] grids = new Set[3][3];
		
		for(int i = 0; i < 3; i++) {
			grids[i] = new Set[3];
			for(int j = 0; j < 3; j++) {
				grids[i][j] = new HashSet<Integer>();
				for(int n = 1; n <= 9; n++) {
					grids[i][j].add(n);
				}
			}
		}
		
		for(int i = 0; i < 9; i++) {
			rows[i] = new HashSet<Integer>();
			cols[i] = new HashSet<Integer>();
			
			for(int j = 1; j <= 9; j++) {
				rows[i].add(j);
				cols[i].add(j);
			}
		}
		
		for(int i = 0; i < 9; i++) {
			for(int j = 0; j < 9; j++) {
				if(board[i][j] == '.') {
					
				} else {
					int num = Character.getNumericValue(board[i][j]);
					if(grids[i/3][j/3].contains(num) == false || rows[i].contains(num) == false || cols[j].contains(num) == false) {
						return false;
					}
					rows[i].remove(num);
					cols[j].remove(num);
					grids[i/3][j/3].remove(num);
				}
			}
		}
		
		for(int i = 0; i < 9; i++) {
			for(int j = 0; j < 9; j++) {
				if(board[i][j] == '.') {
					boolean flag = false;
					for(int num = 1; num <= 9; num++) {
						if(grids[i][j].contains(num) && rows[i].contains(num) && cols[j].contains(num)) {
							flag = true;
							break;
						}
					}
					if(flag == false) {
						return false;
					}
				}
			}
		}
		
		return true;
		
		
	
	}

}
