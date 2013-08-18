
public class Solution {
	public int searchInsert(int[] A, int target) {
		
		return binarySearch(A, target, 0, A.length - 1);
	}
	
	private int binarySearch(int[] A, int target, int low, int high) {
		if(high <= low) {
			if(target > A[low]) {
				return low+1;
			} else {
				return low;
			}
		} else {
			int mid = (low + high) / 2;
			int v = A[mid];
			if(target < v) {
				return binarySearch(A, target, low, mid);
			} else if(target == mid) {
				return mid;
			} else {
				return binarySearch(A, target, mid, high);
			}
		}
	}

}
