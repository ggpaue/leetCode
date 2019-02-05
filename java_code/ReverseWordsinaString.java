/**
 * 
 * @author GGPAUE
 * 
 * Given an input string, reverse the string word by word.
 * 
 * For example,
 * Given s = "the sky is blue",
 * return "blue is sky the".
 * 
 */

public class Solution {
	public String reverseWords(String s) {
		if(s.isEmpty() || s.length() == 0) return s;
		StringBuilder sb = new StringBuilder();
		int t, h;
		for(int i = s.length() - 1; i >= 0; i--) {
			while(i >= 0 && s.charAt(i) == ' ') i--;
			
			if(i < 0) break;
			t = i;
			h = t;
			
			while(i >= 0 && s.charAt(i) != ' ') {
				h = i;
				i--;
			}
			
			if(h <= t && sb.length() > 0) sb.append(' ');
			for(int j = h; j <= t; j++) {
				sb.append(s.charAt(j));
			}
		}
		return sb.toString();
	}

}
