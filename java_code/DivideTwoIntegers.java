/**
 * 
 * @author GGPAUE
 * Divide two integers without using multiplication, division and mod operator.
 *
 */

public class Solution {
	public int divide(int dividend, int divisor) {
		long a = Math.abs((long) dividend);
		long b = Math.abs((long) divisor);
		
		long[] result = dividePos(a, b);
		long temp = dividend > 0 && divisor < 0 || dividend < 0 && divisor > 0 ? -result[0] : result[0];
		return (int) temp;
	}
	
	public long[] dividePos(long a, long b) {
		long[] result = new long[2];
		if(a < b) {
			result[0] = 0;
			result[1] = a;
		} else if(a == b) {
			result[0] = 1;
			result[1] = 0;
		} else {
			long[] temp = dividePos(a >> 1, b);
			result[0] = temp[0] << 1;
			result[1] = temp[1] << 1;
			if((a & 1) == 1) result[1] += 1;
			if(result[1] >= b) {
				result[0] += 1;
				result[1] -=b;
			}
		}
		return result;
	}

}
