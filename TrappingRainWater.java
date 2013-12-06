
public class Solution {
	public int trap(int[] A) {
		int result = 0;
		if(A.length < 3) return result;
		
		int[] left = new int[A.length - 2];
		int[] right = new int[A.length - 2];
		
		for(int i = 0; i < A.length - 2; i++) {
			left[i] = i > 0 ? Math.max(left[i - 1], A[i]) : A[i];
		}
		
		for(int i = A.length - 3; i >= 0; i--) {
			right[i] = i < A.length - 3 ? Math.max(right[i + 1], A[i + 2]) : A[i + 2];
		}
		
		for(int i = 0; i < A.length - 2; i++) {
			int temp = Math.min(left[i], right[i]);
			if(temp > A[i + 1]) {
				result += temp - A[i + 1];
			}
		}
		
		return result;
	}

}
