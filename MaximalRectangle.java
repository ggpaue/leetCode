/**
 * 
 * @author GGPAUE
 * Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.
 */
public class Solution {
	public int maximalRectangle(char[][] matrix) {
		int row = matrix.length;
		if(row == 0) return 0;
		int col = matrix[0].length;
		int[][] map = new int[row][col];
		int area = 0;
		for(int j = 0; j < col; j++) {
			map[0][j] = matrix[0][j] == '0' ? 0 : 1;
		}
		for(int i = 1; i < row; i++) {
			for(int j = 0; j < col; j++) {
				map[i][j] = matrix[i][j] == '0' ? map[i - 1][j] : map[i - 1][j] + 1;
			}
		}
		int[] line = new int[col];
		
		for(int i = 0; i < row; i++) {
			for(int j = i; j < row; j++) {
				for(int k = 0; k < col; k++) {
					line[k] = map[j][k] - (i == 0 ? 0 : map[i - 1][k]);
				}
				int count = 0;
			
				for(int k = 0; k < col; k++) {
					if(line[k] == j - i + 1) {
						area = Math.max(area, ++count * (j - i + 1));
					} else {
						area = Math.max(area, count * (j - i + 1));
						count = 0;
					}
				}
				
			}
		}
		return area;
	}

}
