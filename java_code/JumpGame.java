/**
<<<<<<< HEAD
Jump Game
=======
Jump Game 
>>>>>>> a2d7bcbc3dbcb5b45a163bca33c26f40290db5d3
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.


**/


public class Solution {
	public boolean canJump(int [] A) {
		int len = A.length;
		if(len < 1) {
			return true;
		} else {
			int[] record = new int[len];
			int result = solve(A, record, len-1);
			return result == 1 ? true : false;
			
		}
	}
	
	private int solve(int[] A, int[] record, int target) {
		if(record[target] == 0) {
			if(target == 0) {
				record[target] = 1;
			} else {
				for(int i = 0; i<= target-1; i++) {
					int t = solve(A,record, i);
					if(A[i]+i >= target && t==1) {
						record[target] = 1;
						break;
					}
				}
				if(record[target] != 1) record[target] = 2;
			}
			
		}
		return record[target];
	}

}
