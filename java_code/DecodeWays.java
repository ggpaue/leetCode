/**
 * 
 * @author GGPAUE
 * 
 * A message containing letters from A-Z is being encoded to numbers using the following mapping:
 * 
 * 'A' -> 1
 * 'B' -> 2
 * ...
 * 'Z' -> 26
 * Given an encoded message containing digits, determine the total number of ways to decode it.
 * 
 * For example,
 * Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
 * 
 * The number of ways decoding "12" is 2.
 * 
 * 
 */
public class Solution {
	public int numDecodings(String s) {
		if(s.length() == 0) return 0;
		
		int[] hist = new int[2];
		hist[0] = 1;
		hist[1] = 1;
		
		for(int i = 0; i < s.length(); i++) {
			int temp = 0;
			if(s.charAt(i) != '0') temp += hist[1];
			if(i > 0) {
				int a = Integer.parseInt(s.substring(i - 1, i + 1));
				if(s.charAt(i - 1) != '0' && a >= 1 && a <= 26) temp += hist[0];
			}
			hist[0] = hist[1];
			hist[1] = temp;
		}
		return hist[1];
	}
	
	

}
