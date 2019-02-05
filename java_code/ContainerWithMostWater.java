/**
 * 
 * @author GGPAUE
 * 
 * Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
 * 
 * Note: You may not slant the container.
 * 
 */

public class Solution {
	public int maxArea(int[] height) {
		int start = 0;
		int end = height.length - 1;
		int result = 0;
		
		while(start < end) {
			int min = Math.min(height[start], height[end]);
			result = Math.max(result, (end - start) * min);
			if(height[start] < height[end]) {
				while(start < end && height[start] <= min) start++;
			} else if(height[start] > height[end]) {
				while(start < end && height[end] <= min) end--;
			} else {
				while(start < end && height[start] <= min) start++;
				while(start < end && height[end] <= min) end--;
			}
		}
		return result;
	}

}
