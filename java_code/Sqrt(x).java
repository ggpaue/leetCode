
/*
* Implement int sqrt(int x).

* Compute and return the square root of x.
*
*/

public class Solution {
	public int sqrt(int x) {
		int low = 0;
		int high = x;
		while(low <= high) {
			long mid = low + (high - low) / 2;
			long result = mid * mid;
			if(result == x) {
				return (int)mid;
			} else if(result > x) {
				high = (int)mid - 1;
			} else {
				low = (int)mid + 1;
			}
		}
		return (int) high;
	}

}
