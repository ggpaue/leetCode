/**
 * 
 * The set [1,2,3,É,n] contains a total of n! unique permutations.

 * By listing and labeling all of the permutations in order,
 * We get the following sequence (ie, for n = 3):

 * "123"
 * "132"
 * "213"
 * "231"
 * "312"
 * "321"
 * Given n and k, return the kth permutation sequence.

 * Note: Given n will be between 1 and 9 inclusive.
 * 
 */


import java.util.LinkedList;


public class Solution {
	public String getPermutation(int n, int k) {
		LinkedList<Integer> numbers = new LinkedList<Integer>();
		for(int i = 0; i < n; i++) {
			numbers.add(i + 1);
		}
		
		return getPrefix(numbers, k - 1);
	}
	
	public static String getPrefix(LinkedList<Integer> numbers, int k) {
		StringBuilder str = new StringBuilder();
		while(numbers.isEmpty() == false) {
			int product = 1;
			int count = numbers.size();
			while(count >= 1) {
				product *= count;
				count--;
			}
			int prefixRange = product / numbers.size();
			int prefixIndex = k / prefixRange;
			int element = numbers.get(prefixIndex);
			str.append(element);
			numbers.remove(prefixIndex);
			int prefixStart = k / prefixRange * prefixRange;
			k = k - prefixStart;
		}
		return str.toString();
	}

}
