/**

Set Matrix ZeroesApr 6 '12
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.

Follow up:
Did you use extra space?
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

**/

public class Solution {
    public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        if(m == 0)return;
        int n = matrix[0].length;
        if(n == 0 ) return;
        
        boolean col = false,row = false;
        
        for(int i = 0; i < m;i++){
            if(matrix[i][0] == 0){
                col = true;
                break;
            }
        }
        for(int j = 0; j < n;j++){
            if(matrix[0][j] == 0){
                row = true;
                break;
            }
        }
        
        for(int i = 1; i < m ; i++){
            boolean flag = false;
            for(int j = 0; j <  n; j++){
                if(matrix[i][j] == 0){
                    matrix[0][j] = 0;
                    flag = true;
                }
            }
            if(flag == true){
                for(int j = 0; j < n; j++)matrix[i][j] = 0;
            }
        }
        
        for(int j = 0; j < n ; j++){
            if(matrix[0][j] == 0){
                for(int i = 1; i < m;i++){
                    matrix[i][j] = 0;
                }
            }
        }
        
        if(row == true){
            for(int j = 0; j < n;j++){
                matrix[0][j] = 0;
            }
        }
        if(col == true){
            for(int i = 0; i < m;i++){
                matrix[i][0] = 0;
            }
        }
    }
    
}
