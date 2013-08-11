/**
 * 
 * Given two sorted integer arrays A and B, merge B into A as one sorted array.
 *
 *Note:
 *You may assume that A has enough space to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.
 *
 */

public class Solution {
    public void merge(int A[], int m, int B[], int n) {
		int k = m+n-1;
        int aIndex = m-1, bIndex = n-1;
        while(aIndex >= 0 && bIndex >=0) {
        	if(A[aIndex] > B[bIndex]) {
        		A[k] = A[aIndex];
        		aIndex--;
        	} else {
        		A[k] = B[bIndex];
        		bIndex--;
        	}
        	k--;
        }
        while(bIndex >= 0) {
        	A[k] = B[bIndex];
        	bIndex--;
        	k--;
        }
    }
}