/**
 * 
 * @author GGPAUE
 *
 * Follow up for "Remove Duplicates":
 * What if duplicates are allowed at most twice?

 * For example,
 * Given sorted array A = [1,1,1,2,2,3],

 * Your function should return length = 5, and A is now [1,1,2,2,3].
 *
 */

public class Solution {
	public int removeDuplicates(int[] A) {
		if(A.length <= 2) return A.length;
		int i = 0;
		int j = 1;
		int count = 1;
		while(j < A.length) {
			if(A[j] == A[i]) {
				if(count == 2) {
					++j;
				} else {
					++count;
					++i;
					A[i] = A[j];
					++j;
				}
			} else {
				++i;
				A[i] = A[j];
				++j;
				count = 1;
			}
		}
		return i+1;
		
		
	}

}
