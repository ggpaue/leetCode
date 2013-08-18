
public class Solution {
	public int searchInsert(int[] A, int target) {
		int index = 0;
		if(target < A[0]) {
			return 0;
		}
		if(target > A[A.length - 1]) {
			return A.length;
		}
		for(int i=0; i<A.length; i++) {
			if(A[i] == target) {
				index = i;
                break;
			}
			if(A[i] < target && A[i+1] > target) {
				index = i+1;
                break;
			}
			
		}
		return index;
		
	}
	
	

}
