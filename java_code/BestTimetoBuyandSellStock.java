/**
 * 
 * @author GGPAUE
 * Say you have an array for which the ith element is the price of a given stock on day i.

 * If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
 *
 *
 */
public class Solution {
	public int maxProfit(int[] prices) {
		if(prices == null) return 0;
		int len = prices.length;
		int result = getMaxProfit(prices, 0, len);
		return result;
	}
	public static int getMaxProfit(int[] prices, int left, int right) {
		int len = right - left;
		if(len <= 1) return 0;
		int mid = (right + left) / 2;
		
		int minValue = prices[mid];
		int maxValue = prices[mid];
		for(int i=mid; i >= left; i--) {
			if(prices[i] < minValue) {
				minValue = prices[i];
			}
		}
		
		for(int j=mid; j < right; j++) {
			if(prices[j] > maxValue) {
				maxValue = prices[j];
			}
		}
		
		int leftMax = getMaxProfit(prices, left, mid);
		int rightMax = getMaxProfit(prices, mid, right);
		
		int midMax = maxValue - minValue;
		int max = 0;
		max = Math.max(leftMax, rightMax);
		max = Math.max(max, midMax);
		max = Math.max(0, max);
		return max;
	}

}
