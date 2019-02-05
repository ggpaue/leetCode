/**
 * 
 * @author GGPAUE
 * Follow up for "Search in Rotated Sorted Array":
 * What if duplicates are allowed?
 *
 * Would this affect the run-time complexity? How and why?
 *
 * Write a function to determine if a given target is in the array.
 *
 */

public class Solution {
	public boolean search(int[] A, int target) {
		int low = 0;
		int high = A.length - 1;
		int mid = 0;
		while(low <= high) {
			mid = (low + high) / 2;
			if(A[mid] == target) {
				return true;
			} else if(A[low] < A[mid]) {
				if(target >= A[low] && target < A[mid]) {
					high = mid - 1;
				} else {
					low = mid + 1;
				}
			} else if(A[low] > A[mid]) {
				if(target > A[mid] && target <= A[high]) {
					low = mid + 1;
				} else {
					high = mid - 1;
				}
			} else {
				low++;
			}
			
		}
		return false;
	}

}
