/**
 * 
 * @author GGPAUE
 * 
 * Implement strStr().
 *
 * Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.
 *
 */

public class Solution {
	public String strStr(String haystack, String needle) {
		assert(haystack != null && needle != null);
		if(needle.length() == 0) return haystack;
		int i = 0;
		int len1 = haystack.length();
		int len2 = needle.length();
		
		while(i < len1) {
			if(len1 - i < len2) {
				break;
			}
			
			if(haystack.charAt(i) == needle.charAt(0)) {
				int j = i;
				while(j - i < needle.length() && haystack.charAt(j) == needle.charAt(j - i)) {
					j++;
				}
				if(j - i == needle.length()) return haystack.substring(i);
			}
			i++;
		}
		return null;
	}

}
