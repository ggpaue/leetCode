/**
 * 
 * @author GGPAUE
 * Given an array of non-negative integers, you are initially positioned at the first index of the array.
 * 
 * Each element in the array represents your maximum jump length at that position.
 * 
 * Your goal is to reach the last index in the minimum number of jumps.
 * 
 * For example:
 * Given array A = [2,3,1,1,4]
 * 
 * The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)
 */

public class Solution {
	public int jump(int[] A) {
		int result = 1;
		int len = A.length;
		int cur = 0;
		if(len == 0 || A[0] == 0 || len == 1) return 0;
		
		while(cur + A[cur] < len - 1) {
			int record = -1;
			int max = 0;
			for(int i = cur + 1; i <= cur + A[cur]; i++) {
				if(A[i] == 0) 
					continue;
				int temp = i + A[i];
				if(temp > max) {
					max = temp;
					record = i;
				}
			}
			
			if(record == -1 || A[record] == 0) return 0;
			
			result++;
			cur = record;
		}
		return result;
	}

}
