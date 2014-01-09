/*
 * 
 * There are N children standing in a line. Each child is assigned a rating value.
 * 
 * You are giving candies to these children subjected to the following requirements:
 * 
 * Each child must have at least one candy.
 * Children with a higher rating get more candies than their neighbors.
 * What is the minimum candies you must give?
 */

public class Solution {
	public int candy(int[] ratings) {
		int len = ratings.length;
		if(len == 0 || len == 1) return len;
		
		// every child has at least one candy
		int result = len;
		int[] candies = new int[len];
		
		// scan from head to tail, compare each child's rating with their neighbor
		int cur = 0;
		for(int i = 1; i < len; i++) {
			if(ratings[i - 1] < ratings[i]) {
				cur++;
			} else {
				cur = 0;
			}
			candies[i] = cur;
		}
		
		// scan from tail to head, compare child's rating again
		cur = 0;
		for(int i = len - 2; i >= 0; i--) {
			if(ratings[i] > ratings[i + 1]) {
				cur++;
			} else {
				cur = 0;
			}
			// match with both left and right neighbor
			result += Math.max(candies[i], cur);
		}
		
		// add the last position
		result += candies[len - 1];
		return result;
		
	}

}
