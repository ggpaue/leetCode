/**
 * 
 * @author GGPAUE
 * Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

 * Do not allocate extra space for another array, you must do this in place with constant memory.

 * For example,
 * Given input array A = [1,1,2],

 * Your function should return length = 2, and A is now [1,2].
 * 
 */

public class Solution {
	public int removeDuplicates(int[] A) {
		int length = A.length;
		if(length == 0 || length == 1) return length;
		int i = 1;
		for(int j = 1; j < length; j++) {
			if(A[j] != A[j-1]) {
				A[i] = A[j];
				i++;
			}
		}
		if(i < length) A[i] = '\0';
		return i;
	}

}
