
public class Solution {
	public int maxSubArray(int[] A) {
		if(A == null || A.length == 0) {
			return 0;
		} else if(A.length == 1) {
			return A[0];
		}
		int max = Integer.MIN_VALUE;
		int currSum = 0;
		int idx = 0;
		while(idx < A.length) {
			currSum += A[idx];
			max = currSum > max ? currSum : max;
			if(currSum < 0) {
				currSum = 0;
			}
			idx++;
		}
		return max;
		
	}

}
