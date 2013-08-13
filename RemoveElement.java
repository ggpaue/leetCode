/**
Remove Element
Given an array and a value, remove all instances of that value in place and return the new length.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.


**/

import java.util.*;
public class Solution {
	public int removeElement(int[] A, int elem) {
		Arrays.sort(A);
		int left = A.length, right = -1;
		for(int i=0; i<A.length; i++) {
			if(A[i] == elem) {
				left = Math.min(left, i);
				right = Math.max(right, i);
			}
		}
		if(right < 0) {
			return A.length;
		} else {
			int gap = right - left + 1;
			int newSize = A.length - gap;
			for(int j= left; j+gap < A.length; j++) {
				A[j] = A[j+gap];
			}
			return newSize;
		}
		
	}

}
